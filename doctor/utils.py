from datetime import datetime
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone


phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Caracteres inválidos para un número de teléfono.")
 
def valida_cedula(value):
    cedula = str(value)
    if not cedula.isdigit():
        raise ValidationError('La cédula debe contener solo números.')

    longitud = len(cedula)
    if longitud != 10:
        raise ValidationError('Cantidad de dígitos incorrecta.')

    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    total = 0
    for i in range(9):
        digito = int(cedula[i])
        coeficiente = coeficientes[i]
        producto = digito * coeficiente
        if producto > 9:
            producto -= 9
        total += producto

    digito_verificador = (total * 9) % 10
    if digito_verificador != int(cedula[9]):
        raise ValidationError('La cédula no es válida.')
      
def valida_numero_entero_positivo(value):
    if not str(value).isdigit() or int(value) <= 0:
        raise ValidationError('Debe ingresar un número entero positivo válido.')

def valida_numero_flotante_positivo(value):
    try:
        valor_float = float(value)
        if valor_float <= 0:
            raise ValidationError('Debe ingresar un número flotante positivo válido.')
    except ValueError:
        raise ValidationError('Debe ingresar un número flotante válido.')
    
def custom_serializer(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")
    
def save_audit(request, model, action):
    from aplication.core.models import AuditUser
    user = request.user
    # Obtain client ip address
    client_address = ip_client_address(request)
    # Registro en tabla Auditora BD
    auditusuariotabla = AuditUser(usuario=user,
                                         tabla=model.__class__.__name__,
                                         registroid=model.id,
                                         accion=action,
                                         fecha=timezone.now().date(),
                                         hora=timezone.now().time(),
                                         estacion=client_address)
    auditusuariotabla.save()

# Obtener el IP desde donde se esta accediendo
def ip_client_address(request):
    try:
        # case server externo
        client_address = request.META['HTTP_X_FORWARDED_FOR']
    except:
        # case localhost o 127.0.0.1
        client_address = request.META['REMOTE_ADDR']

    return client_address   

from django.core.mail import EmailMessage
from doctor.utils import save_audit
from django.contrib import messages
import logging
from django.template.loader import render_to_string


logger = logging.getLogger(__name__)  # Colocar el logger fuera de las clases

def enviar_correo_confirmacion_html(usuario, fecha_cita, hora_cita):
    try:
        asunto = "Confirmación de tu cita"
        html_mensaje = render_to_string(
            "correo_confirmacion.html",
            {"usuario": usuario, "fecha_cita": fecha_cita, "hora_cita": hora_cita},
        )
        correo = EmailMessage(
            asunto, html_mensaje, "suarezivandario@gmail.com", [usuario.email]
        )
        correo.content_subtype = "html"
        correo.send()
        logger.info(f"Correo enviado exitosamente a {usuario.email}")
    except Exception as e:
        logger.error(f"Error al enviar correo: {e}")
