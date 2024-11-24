from django.urls import reverse_lazy
from aplication.core.forms.tipocategoria import TipoCategoriaForm
from aplication.core.models import TipoCategoria
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class TipoCategoriaExamenListView(ListView):
    template_name = "core/tipocategoria/list.html"
    model = TipoCategoria
    context_object_name = 'categorias'
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
        context['title1'] = "Consulta de Tipo de Categorias"
        return context
    
class TipoCategoriaExamenCreateView(CreateView):
    model = TipoCategoria
    template_name = 'core/tipocategoria/form.html'
    form_class = TipoCategoriaForm
    success_url = reverse_lazy('core:tipocategoria_list')
    # permission_required = 'add_supplier' # en PermissionMixn se verfica si un grupo tiene el permiso

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Crear Tipo Categoria Examen?'
        context['grabar'] = 'Grabar Tipo Categoria Examen'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # print("entro al form_valid")
        response = super().form_valid(form)
        tipocategoria = self.object
        save_audit(self.request, tipocategoria, action='A')
        messages.success(self.request, f"Éxito al crear el tipo de categoria examen {tipocategoria.nombre}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class TipoCategoriaExamenUpdateView(UpdateView):
    model = TipoCategoria
    template_name = 'core/tipocategoria/form.html'
    form_class = TipoCategoriaForm
    success_url = reverse_lazy('core:tipocategoria_list')
    # permission_required = 'change_patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Tipo Categoria Examen'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        tipocategoria = self.object
        save_audit(self.request, tipocategoria, action='M')
        messages.success(self.request, f"Éxito al Modificar el tipo de categoria examen {tipocategoria.nombre}.")
        print("mande mensaje")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al Modificar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class TipoCategoriaExamenDeleteView(DeleteView):
    model = TipoCategoria
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:tipocategoria_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar tipo categoria examen'
        context['description'] = f"¿Desea Eliminar el tipo de categoria examen {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente el tipo de categoria examen {self.object.name}."
        messages.success(self.request, success_message)
        # Cambiar el estado de eliminado lógico
        # self.object.deleted = True
        # self.object.save()
        return super().delete(request, *args, **kwargs)
    
class TipoCategoriaExamenDetailView(DetailView):
    model = TipoCategoria
    
    def get(self, request, *args, **kwargs):
        tipocategoria = self.get_object()
        data = {
            'id': tipocategoria.id,
            'categoria_examen': tipocategoria.id,
            'nombre': tipocategoria.nombre,
            'descripcion': tipocategoria.descripcion,
            'valor_minimo': tipocategoria.valor_minimo,
            'valor_maximo': tipocategoria.valor_maximo,
            # Añade más campos según tu modelo
        }
        return JsonResponse(data)