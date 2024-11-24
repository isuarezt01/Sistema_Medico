from django.urls import reverse_lazy
from aplication.core.forms.btype import BtypeForm
from aplication.core.models import TipoSangre
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class BtypeListView(ListView):
    template_name = "core/BloodType/list.html"
    model = TipoSangre
    context_object_name = 'tipoSangre'
    query = None
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Tipos de Sangre"
        return context
    
class BtypeCreateView(CreateView):
    model = TipoSangre
    template_name = 'core/BloodType/form.html'
    form_class = BtypeForm
    success_url = reverse_lazy('core:type_list')
    # permission_required = 'add_supplier' # en PermissionMixn se verfica si un grupo tiene el permiso

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Crear Tipo Sangre?'
        context['grabar'] = 'Grabar Tipo Sangre'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # print("entro al form_valid")
        response = super().form_valid(form)
        type = self.object
        save_audit(self.request, type, action='A')
        messages.success(self.request, f"Éxito al crear al el tipo de sangre {type.tipo}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class BtypeUpdateView(UpdateView):
    model = TipoSangre
    template_name = 'core/BloodType/form.html'
    form_class = BtypeForm
    success_url = reverse_lazy('core:type_list')
    # permission_required = 'change_patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Tipo de Sangre'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        type = self.object
        save_audit(self.request, type, action='M')
        messages.success(self.request, f"Éxito al Modificar el tipo de sangre {type.tipo}.")
        print("mande mensaje")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al Modificar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class BtypeDeleteView(DeleteView):
    model = TipoSangre
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:type_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Tipo de sangre?'
        context['description'] = f"¿Desea Eliminar el tipo de sangre: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar el tipo de sangre: {self.object.name}."
        messages.success(self.request, success_message)
        # Cambiar el estado de eliminado lógico
        # self.object.deleted = True
        # self.object.save()
        return super().delete(request, *args, **kwargs)
    
class BtypeDetailView(DetailView):
    model = TipoSangre
    
    def get(self, request, *args, **kwargs):
        tipo = self.get_object()
        data = {
            'id': tipo.id,
            'tipo': tipo.tipo,
            'descripcion': tipo.descripcion,
            # Añade más campos según tu modelo
        }
        return JsonResponse(data)