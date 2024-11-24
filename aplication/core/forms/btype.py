from django.forms import ModelForm, ValidationError
from django import forms

from aplication.core.models import TipoSangre

class BtypeForm(ModelForm):
    
    class Meta:    
        model = TipoSangre
        # campos que se muestran en este mismo orden en el formulario como etiquetas html
        fields = ["tipo","descripcion"]
     
        # Mensajes de error personalizados para ciertos campos
        error_messages = {
            "tipo": {
                "unique": "Ya existe ese tipo de sangre.",
            },
        }
        widgets = {
            "tipo": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese Tipo de Sangre",
                    "id": "id_tipo",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "descripcion": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese su descripcion",
                    "id": "id_descripcion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),}      
    
    
