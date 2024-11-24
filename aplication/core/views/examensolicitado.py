from django.urls import reverse_lazy
from aplication.core.forms.examensolicitado import ExamenSolicitadoForm 
from aplication.attention.models import ExamenSolicitado
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class ExamenSolicitadotListView(ListView):
    template_name = "core/examensolicitado/list.html"
    model = ExamenSolicitado
    context_object_name = 'examenessolicitados'
    query = None
    paginate_by = 10
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q') # ver
        
        if q1 is not None: 
            self.query.add(Q(nombre_examen__icontains=q1), Q.AND)   
        return self.model.objects.filter(self.query).order_by('nombre_examen')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Consulta de Examenes"
        return context
    
class ExamenSolicitadoCreateView(CreateView):
    model = ExamenSolicitado
    template_name = 'core/examensolicitado/form.html'
    form_class = ExamenSolicitadoForm
    success_url = reverse_lazy('core:examensolicitado_list')
    # permission_required = 'add_supplier' # en PermissionMixn se verfica si un grupo tiene el permiso

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Crear Examen?'
        context['grabar'] = 'Grabar Examen'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # print("entro al form_valid")
        response = super().form_valid(form)
        examen = self.object
        save_audit(self.request, examen, action='A')
        messages.success(self.request, f"Éxito al crear al paciente {examen.nombre_examen}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class ExamenSolicitadoUpdateView(UpdateView):
    model = ExamenSolicitado
    template_name = 'core/examensolicitado/form.html'
    form_class = ExamenSolicitadoForm
    success_url = reverse_lazy('core:examensolicitado_list')
    # permission_required = 'change_patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Examen'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        examen = self.object
        save_audit(self.request, examen, action='M')
        messages.success(self.request, f"Éxito al Modificar el examen {examen.nombre_examen}.")
        print("mande mensaje")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al Modificar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class ExamenSolicitadoDeleteView(DeleteView):
    model = ExamenSolicitado
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:examensolicitado_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Examen'
        context['description'] = f"¿Desea Eliminar el examen: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente el examen {self.object.name}."
        messages.success(self.request, success_message)
        # Cambiar el estado de eliminado lógico
        # self.object.deleted = True
        # self.object.save()
        return super().delete(request, *args, **kwargs)
    
class ExamenSolicitadoDetailView(DetailView):
    model = ExamenSolicitado
    
    def get(self, request, *args, **kwargs):
        examen = self.get_object()
        data = {
            'id': examen.id,
            'nombre_examen': examen.nombre_examen,
            'fecha_solicitud': examen.fecha_solicitud,
            'comentario': examen.comentario,
            'estado': examen.estado,
            # Añade más campos según tu modelo
        }
        return JsonResponse(data)