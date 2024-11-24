from django.urls import reverse_lazy
from aplication.core.forms.cargo import CargoForm  # Asegúrate de crear este formulario
from aplication.core.models import AuditUser
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q

from doctor.utils import save_audit

class AuditoriaListView(ListView):
    template_name = "core/auditoria/list.html"
    model = AuditUser
    context_object_name = 'auditorias'
    paginate_by = 10
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q') # ver

        if q1 is not None: 
            self.query.add(Q(usuario__icontains=q1), Q.AND)   
        return self.model.objects.filter(self.query).order_by('usuario')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Gestión de Auditorias"
        context['title1'] = "Consulta de CAuditorias"
        return context

    

class AuditoriaDetailView(DetailView):
    model = AuditUser
    
    def get(self, request, *args, **kwargs):
        auditoria = self.get_object()
        data = {
            'id': auditoria.id,
            'usuario': str(auditoria.usuario),
            'tabla': auditoria.tabla,
            'registroid': auditoria.registroid,
            'accion': auditoria.accion,
            'fecha': auditoria.fecha,
            'hora': auditoria.hora,
            'estacion': auditoria.estacion,
        }
        return JsonResponse(data)
