from django.forms import ModelForm, ValidationError
from django import forms
from aplication.core.models import Doctor  # Asegúrate de importar el modelo correcto

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = [
            "nombres", "apellidos", "cedula", "especialidad", 
            "telefonos", "email", "direccion", "activo","fecha_nacimiento", "codigoUnicoDoctor","foto"
        ]
        error_messages = {
            "email": {
                "unique": "Ya existe un doctor registrado con este email.",
            },
        }
        widgets = {
            "nombres": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese nombres",
                    "id": "id_nombres",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12",
                }
            ),
            "apellidos": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese apellidos",
                    "id": "id_apellidos",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12",
                }
            ),
            "cedula": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese cédula",
                    "id": "id_cedula",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12",
                }
            ),
            "codigoUnicoDoctor": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese codigoUnicoDoctor",
                    "id": "id_codigoUnicoDoctor",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12",
                }
            ),
            # Cambia Select a SelectMultiple para permitir selección múltiple
            "especialidad": forms.CheckboxSelectMultiple(
                attrs={
                    "id": "id_especialidad",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full",
                }
            ),
            "fecha_nacimiento": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            "telefonos": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese teléfono o celular",
                    "id": "id_telefonos",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Ingrese correo electrónico",
                    "id": "id_email",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12",
                }
            ),
            "direccion": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese dirección",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12",
                }
            ),
            "foto": forms.FileInput(
                attrs={
                    "type": "file",
                    "id": "id_foto",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "activo": forms.CheckboxInput(
                attrs={
                    "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                }
            ),
        }
        labels = {
            "cedula": "DNI",
        }

    def clean_nombres(self):
        nombres = self.cleaned_data.get("nombres")
        if not nombres or len(nombres) < 2:
            raise ValidationError("El nombre debe tener al menos 2 caracteres.")
        return nombres.upper()

    def clean_apellidos(self):
        apellidos = self.cleaned_data.get("apellidos")
        if not apellidos or len(apellidos) < 1:
            raise ValidationError("El apellido debe tener al menos 1 carácter.")
        return apellidos.upper()
