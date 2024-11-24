from django.urls import reverse_lazy
from aplication.core.forms.tipomedicamento import TipoMedicamentoForm
from aplication.core.models import TipoMedicamento
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class TipoMedicamentoListView(ListView):
    template_name = "core/tipom/list.html"
    model = TipoMedicamento
    context_object_name = 'medicamentos'
    query = None
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Consulta de Medicamentos"
        return context
    
class TipomedicamentoCreateView(CreateView):
    model = TipoMedicamento
    template_name = 'core/tipom/form.html'
    form_class = TipoMedicamentoForm
    success_url = reverse_lazy('core:tipom_list')
    # permission_required = 'add_supplier' # en PermissionMixn se verfica si un grupo tiene el permiso

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Crear Tipo Medicamento?'
        context['grabar'] = 'Grabar el Tipo de Medicamento'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # print("entro al form_valid")
        response = super().form_valid(form)
        medicamento = self.object
        save_audit(self.request, medicamento, action='A')
        messages.success(self.request, f"Éxito al crear el tipo de medicamento {medicamento.nombre}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class TipoMedicamentotUpdateView(UpdateView):
    model = TipoMedicamento
    template_name = 'core/tipom/form.html'
    form_class = TipoMedicamentoForm
    success_url = reverse_lazy('core:tipom_list')
    # permission_required = 'change_patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Medicamento'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        medicamento = self.object
        save_audit(self.request, medicamento, action='M')
        messages.success(self.request, f"Éxito al Modificar el medicamento {medicamento.nombre}.")
        print("mande mensaje")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al Modificar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class TipoMedicamentoDeleteView(DeleteView):
    model = TipoMedicamento
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:tipom_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Medicamento'
        context['description'] = f"¿Desea Eliminar el medicamento? : {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar el medicamento {self.object.name}."
        messages.success(self.request, success_message)
        # Cambiar el estado de eliminado lógico
        # self.object.deleted = True
        # self.object.save()
        return super().delete(request, *args, **kwargs)
    
class TipoMedicamentoDetailView(DetailView):
    model = TipoMedicamento
    
    def get(self, request, *args, **kwargs):
        tipom = self.get_object()
        data = {
            'id': tipom.id,
            'nombre': tipom.nombre,
            'descripcion': tipom.descripcion,
            # Añade más campos según tu modelo
        }
        return JsonResponse(data)