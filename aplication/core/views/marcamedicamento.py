from django.urls import reverse_lazy
from aplication.core.forms.marcamedicamento import MarcaMedicamentoForm
from aplication.core.models import MarcaMedicamento
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class MarcaMedicamentoListView(ListView):
    template_name = "core/marcamedicamento/list.html"
    model = MarcaMedicamento
    context_object_name = 'marcamedicamentos'
    query = None
    paginate_by = 10
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q') # ver
        
        if q1 is not None: 
            self.query.add(Q(nombre__icontains=q1), Q.AND)   
        return self.model.objects.filter(self.query).order_by('nombre')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Consulta de Marca de Medicamentos"
        return context
    
class MarcaMedicamentoCreateView(CreateView):
    model = MarcaMedicamento
    template_name = 'core/marcamedicamento/form.html'
    form_class = MarcaMedicamentoForm
    success_url = reverse_lazy('core:marca_list')
    # permission_required = 'add_supplier' # en PermissionMixn se verfica si un grupo tiene el permiso

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Crear Nueva Marca de Medicamento?'
        context['grabar'] = 'Grabar Marca'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # print("entro al form_valid")
        response = super().form_valid(form)
        marca = self.object
        save_audit(self.request, marca, action='A')
        messages.success(self.request, f"Éxito al crear la marca {marca.nombre}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class MarcaMedicamentoUpdateView(UpdateView):
    model = MarcaMedicamento
    template_name = 'core/marcamedicamento/form.html'
    form_class = MarcaMedicamentoForm
    success_url = reverse_lazy('core:marca_list')
    # permission_required = 'change_patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Marcas'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        patient = self.object
        save_audit(self.request, patient, action='M')
        messages.success(self.request, f"Éxito al Modificar la Marca {patient.nombre}.")
        print("mande mensaje")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al Modificar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class MarcaMedicamentoDeleteView(DeleteView):
    model = MarcaMedicamento
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:marca_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Marca'
        context['description'] = f"¿Desea Eliminar la marca: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente la marca {self.object.name}."
        messages.success(self.request, success_message)
        # Cambiar el estado de eliminado lógico
        # self.object.deleted = True
        # self.object.save()
        return super().delete(request, *args, **kwargs)
    
class MarcaMedicamentoDetailView(DetailView):
    model = MarcaMedicamento
    
    def get(self, request, *args, **kwargs):
        marca = self.get_object()
        data = {
            'id': marca.id,
            'nombre': marca.nombre,
            'descripcion': marca.descripcion,
            # Añade más campos según tu modelo
        }
        return JsonResponse(data)