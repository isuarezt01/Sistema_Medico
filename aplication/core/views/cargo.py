from django.urls import reverse_lazy
from aplication.core.forms.cargo import CargoForm  # Asegúrate de crear este formulario
from aplication.core.models import Cargo
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from doctor.utils import save_audit

class CargoListView(ListView):
    template_name = "core/cargo/list.html"
    model = Cargo
    context_object_name = 'cargos'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Gestión de Cargos"
        context['title1'] = "Consulta de Cargos"
        return context

class CargoCreateView(CreateView):
    model = Cargo
    template_name = 'core/cargo/form.html'
    form_class = CargoForm
    success_url = reverse_lazy('core:cargo_list')
    # permission_required = 'add_supplier' # en PermissionMixn se verfica si un grupo tiene el permiso

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Crear Cargo?'
        context['grabar'] = 'Grabar Crago'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # print("entro al form_valid")
        response = super().form_valid(form)
        cargo = self.object
        save_audit(self.request, cargo, action='A')
        messages.success(self.request, f"Éxito al crear el Cargo {cargo.nombre}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

class CargoUpdateView(UpdateView):
    model = Cargo
    template_name = 'core/cargo/form.html'
    form_class = CargoForm
    success_url = reverse_lazy('core:cargo_list')
    # permission_required = 'change_patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Cargo?'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        cargo = self.object
        save_audit(self.request, cargo, action='M')
        messages.success(self.request, f"Éxito al Modificar el cargo {cargo.nombre}.")
        print("mande mensaje")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al Modificar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class CargoDeleteView(DeleteView):
    model = Cargo
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:cargo_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Cargo?'
        context['description'] = f"¿Desea Eliminar el cargo: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente el cargo {self.object.name}."
        messages.success(self.request, success_message)
        # Cambiar el estado de eliminado lógico
        # self.object.deleted = True
        # self.object.save()
        return super().delete(request, *args, **kwargs)
    

class CargoDetailView(DetailView):
    model = Cargo
    
    def get(self, request, *args, **kwargs):
        cargo = self.get_object()
        data = {
            'id': cargo.id,
            'nombre': cargo.nombre,
            'descripcion': cargo.descripcion,
        }
        return JsonResponse(data)
