from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import View
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from aplication.core.models import Paciente
from aplication.attention.models import Atencion

class FichaMedicaView(View):
    template_name = 'attention/fichamedica/ficha_medica.html'

    def get(self, request, paciente_id):
        paciente = get_object_or_404(Paciente, id=paciente_id)
        atenciones = Atencion.objects.filter(paciente=paciente).order_by('-fecha_atencion')
        
        context = {
            'paciente': paciente,
            'atenciones': atenciones,
        }
        return render(request, self.template_name, context)

def generar_ficha_medica_pdf(request, paciente_id):
    # Obtén el paciente y sus atenciones
    paciente = get_object_or_404(Paciente, id=paciente_id)
    atenciones = Atencion.objects.filter(paciente=paciente).order_by('-fecha_atencion')

    # Configura la respuesta HTTP para enviar el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Ficha_Medica_{paciente.cedula}.pdf"'

    # Crear el PDF con ReportLab
    p = canvas.Canvas(response, pagesize=letter)
    p.setTitle("Ficha Médica")

    # Título
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 750, f"Ficha Médica de {paciente.nombre_completo}")
    p.setFont("Helvetica", 12)

    # Información del Paciente
    p.drawString(100, 730, f"Cédula: {paciente.cedula}")
    p.drawString(100, 710, f"Edad: {paciente.calcular_edad(paciente.fecha_nacimiento)} años")
    p.drawString(100, 690, f"Tipo de Sangre: {paciente.tipo_sangre}")
    p.drawString(100, 670, f"Alergias: {paciente.alergias or 'No registradas'}")

    # Historial de Atenciones
    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, 640, "Historial de Atenciones")

    y = 620  # Posición vertical inicial para listar atenciones
    p.setFont("Helvetica", 12)

    if atenciones.exists():
        for atencion in atenciones:
            if y < 50:  # Salto de página si es necesario
                p.showPage()
                p.setFont("Helvetica", 12)
                y = 750

            p.drawString(100, y, f"Fecha: {atencion.fecha_atencion.strftime('%d/%m/%Y')}")
            p.drawString(100, y - 20, f"Motivo: {atencion.motivo_consulta}")
            p.drawString(100, y - 40, f"Diagnósticos: {atencion.get_diagnosticos}")
            p.drawString(100, y - 60, f"Tratamiento: {atencion.tratamiento}")
            y -= 100  # Espaciado entre atenciones
    else:
        p.drawString(100, y, "No se encontraron atenciones médicas registradas.")

    # Cerrar el PDF
    p.showPage()
    p.save()

    return response

