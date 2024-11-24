from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from aplication.core.forms.doctor import DoctorForm
from aplication.core.models import Doctor
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class DoctorListView(ListView):
    template_name = "core/doctor/list.html"
    model = Doctor
    context_object_name = 'doctores'
    query = None
    paginate_by = 10
    
    def get_queryset(self):
        self.query = Q()
        q = self.request.GET.get('q')
        if q:
            self.query.add(Q(nombres__icontains=q) | Q(apellidos__icontains=q) | Q(cedula__icontains=q), Q.AND)
        return self.model.objects.filter(self.query).order_by('apellidos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Gestión Médica"
        context['title1'] = "Consulta de Doctores"
        return context

class DoctorCreateView(CreateView):
    model = Doctor
    template_name = 'core/doctor/form.html'
    form_class = DoctorForm
    success_url = reverse_lazy('core:doctor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Crear Doctor'
        context['grabar'] = 'Registrar Doctor'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        doctor = self.object
        save_audit(self.request, doctor, action='A')
        messages.success(self.request, f"Éxito al crear al doctor {doctor.nombre_completo}.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))

class DoctorUpdateView(UpdateView):
    model = Doctor
    template_name = 'core/doctor/form.html'
    form_class = DoctorForm
    success_url = reverse_lazy('core:doctor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Doctor'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        doctor = self.object
        save_audit(self.request, doctor, action='M')
        messages.success(self.request, f"Éxito al modificar el doctor {doctor.nombre_completo}.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al modificar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))

class DoctorDeleteView(DeleteView):
    model = Doctor
    success_url = reverse_lazy('core:doctor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Doctor'
        context['description'] = f"¿Desea eliminar al doctor: {self.object.nombre_completo}?"
        context['back_url'] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente al doctor {self.object.nombre_completo}."
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)

class DoctorDetailView(DetailView):
    model = Doctor

    def get(self, request, *args, **kwargs):
        doctor = self.get_object()
        data = {
            'id': doctor.id,
            'nombres': doctor.nombres,
            'apellidos': doctor.apellidos,
            'cedula': doctor.cedula,
            'direccion': doctor.direccion,
            'codigoUnicoDoctor': doctor.codigoUnicoDoctor,
            'telefonos': doctor.telefonos,
            'email': doctor.email,
            'foto': doctor.get_image(),
        }
        return JsonResponse(data)
