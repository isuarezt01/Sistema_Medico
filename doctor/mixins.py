from django.db.models import Q

# configuracion de contexto generico y permisos de botones
class ListViewMixin(object):
    query = None
    paginate_by = 2
    
    def dispatch(self, request, *args, **kwargs):
        self.query = Q()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = f'Consulta de {self.model._meta.verbose_name_plural}'
        # añade los permisos del grupo activo(add_pais, view_ciudad)
        # print("estoy en el mixing..")
        # print(self.request.session.get('group_id'))
        # context['permissions'] = self._get_permission_dict_of_group() 
        # crear la data y la session con los menus y modulos del usuario 
        # MenuModule(self.request).fill(context)
        return context

    # def _get_permission_dict_of_group(self):
    #     print("user:=",self.request.user)
    #     return GroupPermission.get_permission_dict_of_group(self.request.user)

class CreateViewMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = f'Registro de {self.model._meta.verbose_name}'
        # context['permissions'] = self._get_permission_dict_of_group() #('view_invoice','add_invoice')
        # MenuModule(self.request).fill(context)
        return context

    # def _get_permission_dict_of_group(self):
    #     return GroupPermission.get_permission_dict_of_group(self.request.user)

class UpdateViewMixin(object):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = f'Modificar Nuevo(a) {self.model._meta.verbose_name}'
        # context['permissions'] = self._get_permission_dict_of_group()
        # MenuModule(self.request).fill(context)
        
        return context

    # def _get_permission_dict_of_group(self):
    #     return GroupPermission.get_permission_dict_of_group(self.request.user)
    
class DeleteViewMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = "SaludSync"
        # context['title1'] = f'Eliminacion de {self.model._meta.verbose_name}'
        # context['permissions'] = self._get_permission_dict_of_group()
        # MenuModule(self.request).fill(context)
        return context

    # def _get_permission_dict_of_group(self):
    #     return GroupPermission.get_permission_dict_of_group(self.request.user)