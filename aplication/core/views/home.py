from datetime import date, timedelta
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from aplication.core.models import Paciente
from aplication.attention.models import Atencion, CitaMedica

class HomeTemplateView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "SaludSync"
        context["title1"] = "Sistema Médico"
        context["title2"] = "Sistema Médico"
        context["can_paci"] = Paciente.cantidad_pacientes()
        context["can_atencion"] = Atencion.cantidad_atencion()
        context["ultimo_paciente"] = Paciente.objects.order_by('-id').first()
        context["can_cita"] = CitaMedica.cantidad_cita()
        context["proximas_citas"] = CitaMedica.objects.filter(fecha=date.today(), estado='P').order_by('hora_cita')
        context["ultima_cita_completada"] = CitaMedica.objects.filter(estado='R').order_by('-fecha', '-hora_cita').first()
        context["ultima_cita"] = CitaMedica.objects.order_by('-fecha', '-hora_cita').first()
        return context
    
class ChartDataView(View):
    def get(self, request, *args, **kwargs):
        # Ejemplo: Cantidad de citas médicas por día en los últimos 7 días
        today = date.today()
        labels = []
        data = []
        for i in range(7):
            day = today - timedelta(days=i)
            labels.append(day.strftime('%d/%m'))
            data.append(CitaMedica.objects.filter(fecha=day).count())
        
        return JsonResponse({
            "labels": labels[::-1],  # Invertir el orden para mostrar cronológicamente
            "data": data[::-1]
        })