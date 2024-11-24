from django import forms
from django.forms import ModelForm, ValidationError
from aplication.core.models import Especialidad

# Definición de la clase SpecialityForm que hereda de ModelForm
class SpecialityForm(ModelForm):
    # Clase interna Meta para configurar el formulario
    class Meta:
        model = Especialidad
        fields = ["nombre", "descripcion", "activo"]

        error_messages = {
            "nombre": {
                "unique": "Ya existe una especialidad con este nombre.",
            },
        }

        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Ingrese el nombre de la especialidad",
                "id": "id_nombre",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "descripcion": forms.Textarea(attrs={
                "placeholder": "Ingrese una descripción",
                "id": "id_descripcion",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                "rows": 3,
            }),
            "activo": forms.CheckboxInput(attrs={
                "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            }),
        }

        labels = {
            "nombre": "Nombre de la Especialidad",
        }

    # Método de limpieza para el campo 'nombre'
    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if not nombre or len(nombre) < 2:
            raise ValidationError("El nombre de la especialidad debe tener al menos 2 caracteres.")
        return nombre
