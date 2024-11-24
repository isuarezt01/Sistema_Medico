from django.urls import reverse_lazy
from aplication.core.forms.citamedica import CitaMedicaForm
from aplication.attention.models import CitaMedica
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class CitaMedicaListView(ListView):
    template_name = "core/citamedica/list.html"
    model = CitaMedica
    context_object_name = 'citas'
    query = None
    paginate_by = 10
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q') # ver
        
        if q1 is not None: 
            self.query.add(Q(fecha__icontains=q1), Q.AND)   
        return self.model.objects.filter(self.query).order_by('fecha')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Consulta de Citas"
        return context
    
class CitaMedicaCreateView(CreateView):
    model = CitaMedica
    template_name = 'core/citamedica/form.html'
    form_class = CitaMedicaForm
    success_url = reverse_lazy('core:citamedica_list')
    # permission_required = 'add_supplier' # en PermissionMixn se verfica si un grupo tiene el permiso

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Crear cita medica?'
        context['grabar'] = 'Grabar cita medica'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # print("entro al form_valid")
        response = super().form_valid(form)
        citamedica = self.object
        save_audit(self.request, citamedica, action='A')
        messages.success(self.request, f"Éxito al crear la cita medica del paciente: {citamedica.paciente}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    



class CitaMedicaUpdateView(UpdateView):
    model =CitaMedica
    template_name = 'core/citamedica/form.html'
    form_class = CitaMedicaForm
    success_url = reverse_lazy('core:citamedica_list')
    # permission_required = 'change_patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar cita medica'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        citamedica = self.object
        save_audit(self.request, citamedica, action='M')
        messages.success(self.request, f"Éxito al Modificar la cita medica del paciente : {citamedica.paciente}.")
        print("mande mensaje")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al Modificar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class CitaMedicaDeleteView(DeleteView):
    model = CitaMedica
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:citamedica_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar cita medica'
        context['description'] = f"¿Desea Eliminar la cita medica: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente la cita medica {self.object.name}."
        messages.success(self.request, success_message)
        # Cambiar el estado de eliminado lógico
        # self.object.deleted = True
        # self.object.save()
        return super().delete(request, *args, **kwargs)
    
class CitaMedicaFDetailView(DetailView):
    model = CitaMedica
    
    def get(self, request, *args, **kwargs):
        citamedica = self.get_object()
        data = {
            'id': citamedica.id,
            'fecha': citamedica.fecha,
            'hora_cita': citamedica.hora_cita,
            'estado': citamedica.estado,
            # Añade más campos según tu modelo
        }
        return JsonResponse(data)