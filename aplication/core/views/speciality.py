from django.urls import reverse_lazy
from aplication.core.forms.speciality import SpecialityForm
from aplication.core.models import Especialidad
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class SpecialityListView(ListView):
    template_name = "core/speciality/list.html"
    model = Especialidad
    context_object_name = 'especialidades'
    query = None
    paginate_by = 10

    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q')  # búsqueda
        if q1 is not None:
            self.query.add(Q(nombre__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Gestión de Especialidades"
        context['title1'] = "Consulta de Especialidades"
        return context

class SpecialityCreateView(CreateView):
    model = Especialidad
    template_name = 'core/speciality/form.html'
    form_class = SpecialityForm
    success_url = reverse_lazy('core:speciality_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Crear Especialidad'
        context['grabar'] = 'Grabar Especialidad'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        speciality = self.object
        save_audit(self.request, speciality, action='A')
        messages.success(self.request, f"Éxito al crear la especialidad {speciality.nombre}.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))

class SpecialityUpdateView(UpdateView):
    model = Especialidad
    template_name = 'core/speciality/form.html'
    form_class = SpecialityForm
    success_url = reverse_lazy('core:speciality_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Especialidad'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        speciality = self.object
        save_audit(self.request, speciality, action='M')
        messages.success(self.request, f"Éxito al modificar la especialidad {speciality.nombre}.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al modificar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))

class SpecialityDeleteView(DeleteView):
    model = Especialidad
    success_url = reverse_lazy('core:speciality_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Especialidad'
        context['description'] = f"¿Desea eliminar la especialidad: {self.object.nombre}?"
        context['back_url'] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente la especialidad {self.object.nombre}."
        messages.success(self.request, success_message)
        # Cambiar el estado de eliminado lógico si es necesario
        return super().delete(request, *args, **kwargs)

class SpecialityDetailView(DetailView):
    model = Especialidad

    def get(self, request, *args, **kwargs):
        speciality = self.get_object()
        data = {
            'id': speciality.id,
            'nombre': speciality.nombre,
            'descripcion': speciality.descripcion,
            # Añade más campos según tu modelo
        }
        return JsonResponse(data)
