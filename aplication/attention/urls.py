from django.urls import path
from aplication.attention.models import FichaMedicaView
from aplication.attention.views.fichamedica import generar_ficha_medica_pdf
# from aplication.attention.views.medical_attention import AttentionCreateView, AttentionDetailView, AttentionListView, AttentionUpdateView
from aplication.attention.views.medical_attention import AttentionListView, AttentionCreateView, AttentionUpdateView, AttentionDetailView
from aplication.core.views.home import HomeTemplateView
from aplication.core.views.patient import PatientCreateView, PatientDeleteView, PatientDetailView, PatientListView, PatientUpdateView
from aplication.attention.views.certificado import CertificadoCreateView, CertificadoListView, CertificadoUpdateView, CertificadoDeleteView, CertificadoDetailView, CertificadoPDFView
from aplication.attention.views.PaypalPayment import (
    PagoListView,
    PagoCreateView,
    PagoDetailView,
    PagoDeleteView,
    PagoComprobanteView,
    paypal_execute,
    verificar_pago_paciente,
)
app_name='attention' # define un espacio de nombre para la aplicacion

urlpatterns = [
  # rutas de atenciones
  path('attention_list/',AttentionListView.as_view() ,name="attention_list"),
  path('attention_create/', AttentionCreateView.as_view(),name="attention_create"),
  path('attention_update/<int:pk>/', AttentionUpdateView.as_view(),name='attention_update'),
  path('attention_detail/<int:pk>/', AttentionDetailView.as_view(),name='attention_detail'),
  
  path('patient_delete/<int:pk>/', PatientDeleteView.as_view(),name='patient_delete'),
  
  path('ficha_medica/<int:paciente_id>/', FichaMedicaView.as_view(), name='ficha_medica'),
  path('ficha_medica/pdf/<int:paciente_id>/', generar_ficha_medica_pdf, name='generar_ficha_medica_pdf'),
  
  path('certificado_list/',CertificadoListView.as_view() ,name="certificado_list"),
  path('certificado_create/', CertificadoCreateView.as_view(),name="certificado_create"),
  path('certificado_update/<int:pk>/', CertificadoUpdateView.as_view(),name='certificado_update'),
  path('certificado_delete/<int:pk>/', CertificadoDeleteView.as_view(),name='certificado_delete'),
  path('certificado_detail/<int:pk>/', CertificadoDetailView.as_view(),name='certificado_detail'),
  path('certificado_pdf/<int:pk>/', CertificadoPDFView.as_view(), name='certificado_pdf'),
  
  path('pagos/', PagoListView.as_view(), name='pago_list'),
  path('pagos/crear/', PagoCreateView.as_view(), name='pago_create'),
  path('pagos/detalle/<int:pk>/', PagoDetailView.as_view(), name='pago_detail'),
  path('pagos/eliminar/<int:pk>/', PagoDeleteView.as_view(), name='pago_delete'),
  path('pagos/comprobante/<int:pk>/', PagoComprobanteView.as_view(), name='pago_comprobante'),
  path('paypal/execute/', paypal_execute, name='paypal_execute'),
  path('verificar_pago_paciente/', verificar_pago_paciente, name='verificar_pago_paciente'),
]