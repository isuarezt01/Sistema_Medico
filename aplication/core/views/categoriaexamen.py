from django.urls import reverse_lazy
from aplication.core.forms.categoriaexamen import CategoriaExamenForm
from aplication.attention.models import CategoriaExamen
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class CategoriaExamenListView(ListView):
    template_name = "core/categoriaexamen/list.html"
    model = CategoriaExamen
    context_object_name = 'examenes'
    query = None
    paginate_by = 10
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q') # ver

        if q1 is not None: 
            self.query.add(Q(nombre__icontains=q1),Q.AND)   
        return self.model.objects.filter(self.query).order_by('nombre')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Consulta de Categoria Examen"
        return context
    
class CategoriaExamenCreateView(CreateView):
    model = CategoriaExamen
    template_name = 'core/categoriaexamen/form.html'
    form_class = CategoriaExamenForm
    success_url = reverse_lazy('core:categoriaexamen_list')
    # permission_required = 'add_supplier' # en PermissionMixn se verfica si un grupo tiene el permiso

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Crear Categoria Examen?'
        context['grabar'] = 'Grabar Categoria Examen'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # print("entro al form_valid")
        response = super().form_valid(form)
        categoriaexamen = self.object
        save_audit(self.request, categoriaexamen, action='A')
        messages.success(self.request, f"Éxito al crear la categoria examen {categoriaexamen.nombre}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class CategoriaExamenUpdateView(UpdateView):
    model = CategoriaExamen
    template_name = 'core/categoriaexamen/form.html'
    form_class = CategoriaExamenForm
    success_url = reverse_lazy('core:categoriaexamen_list')
    # permission_required = 'change_patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Categoria Examen'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        categoriaexamen = self.object
        save_audit(self.request, categoriaexamen, action='M')
        messages.success(self.request, f"Éxito al Modificar la categoria examen {categoriaexamen.nombre}.")
        print("mande mensaje")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al Modificar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class CategoriaExamenDeleteView(DeleteView):
    model = CategoriaExamen
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:categoriaexamen_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Proveedorl'
        context['description'] = f"¿Desea Eliminar la categoria examen {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente al categoria examen {self.object.name}."
        messages.success(self.request, success_message)
        # Cambiar el estado de eliminado lógico
        # self.object.deleted = True
        # self.object.save()
        return super().delete(request, *args, **kwargs)
    
class CategoriaExamenDetailView(DetailView):
    model = CategoriaExamen
    
    def get(self, request, *args, **kwargs):
        categoriaexamen = self.get_object()
        data = {
            'id': categoriaexamen.id,
            'nombre': categoriaexamen.nombre,
            'descripcion': categoriaexamen.descripcion,
            # Añade más campos según tu modelo
        }
        return JsonResponse(data)