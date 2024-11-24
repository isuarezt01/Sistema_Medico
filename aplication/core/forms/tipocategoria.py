from django.forms import ModelForm, ValidationError
from django import forms
from aplication.core.models import TipoCategoria

# Definición de la clase PatientForm que hereda de ModelForm
class TipoCategoriaForm(ModelForm):
        # Clase interna Meta para configurar el formulario
    class Meta:    
        model = TipoCategoria
        # campos que se muestran en este mismo orden en el formulario como etiquetas html
        fields = ["categoria_examen","nombre","descripcion","valor_minimo","valor_maximo","activo"]
     
     
        # Personalización de los widgets o etiquetas que se van a mostrar en el formulario html si no se desea el valor por default dado en el modelo
        widgets = {
            "categoria_examen": forms.Select(
                attrs={
                    "placeholder": "Selecione",
                    "id": "id_categoria_examen",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "nombre": forms.TextInput(
                attrs={
                    "placeholder": "Selecione",
                    "id": "id_nombre",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "descripcion": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese descripcion",
                    "id": "id_descripcion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),      
            "valor_minimo": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese valor_minimo",
                    "id": "id_valor_minimo",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),       
            "valor_maximo": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese valor_maximo",
                    "id": "id_valor_maximo",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),       
            "activo": forms.CheckboxInput(
                attrs={
                    "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                }
            ),
        }

# método de limpieza se ejecuta automáticamente cuando Django valida el campo nombres en el formulario al ejecutar el metodo form_valid()
def clean_nombres(self):
    nombre = self.cleaned_data.get("nombre")
    # Verificar si el campo tiene menos de 1 carácter
    if not nombre or len(nombre) < 2:
        raise ValidationError("El nombre debe tener al menos 2 carácter.")
    
    return nombre.upper()
