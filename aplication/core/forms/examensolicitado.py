from django.forms import ModelForm, ValidationError
from django import forms
from aplication.attention.models import ExamenSolicitado

# Definición de la clase PatientForm que hereda de ModelForm
class ExamenSolicitadoForm(ModelForm):
        # Clase interna Meta para configurar el formulario
    class Meta:    
        model = ExamenSolicitado
        # campos que se muestran en este mismo orden en el formulario como etiquetas html
        fields = ["nombre_examen","paciente","resultado","comentario","estado"]
     
     
        # Personalización de los widgets o etiquetas que se van a mostrar en el formulario html si no se desea el valor por default dado en el modelo
        widgets = {
            "nombre_examen": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese nombres",
                    "id": "id_nombre_examen",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "paciente": forms.Select(
                attrs={
                    "placeholder": "Selecione",
                    "id": "id_paciente",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "resultado": forms.FileInput(
                attrs={
                    "placeholder": "Ingrese resultado",
                    "id": "id_resultado",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),      
            "comentario": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese comentario",
                    "id": "id_comentario",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),       
            "estado": forms.Select(
                attrs={
                    "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                }
            ),
        }

# método de limpieza se ejecuta automáticamente cuando Django valida el campo nombres en el formulario al ejecutar el metodo form_valid()
def clean_nombres(self):
    nombre_examen = self.cleaned_data.get("nombre_examen")
    # Verificar si el campo tiene menos de 1 carácter
    if not nombre_examen or len(nombre_examen) < 2:
        raise ValidationError("El nombre debe tener al menos 2 carácter.")
    
    return nombre_examen.upper()
