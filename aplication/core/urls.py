from django.urls import path
from aplication.attention.views.medical_attention import AttentionCreateView, AttentionDetailView, AttentionListView, AttentionUpdateView
from aplication.core.views.home import HomeTemplateView
from aplication.core.views.patient import PatientCreateView, PatientDeleteView, PatientDetailView, PatientListView, PatientUpdateView
from aplication.core.views.btype import BtypeListView, BtypeCreateView, BtypeUpdateView, BtypeDeleteView, BtypeDetailView
from aplication.core.views.speciality import SpecialityListView, SpecialityCreateView, SpecialityDeleteView, SpecialityDetailView, SpecialityUpdateView
from aplication.core.views.doctor import DoctorCreateView, DoctorDeleteView, DoctorListView, DoctorUpdateView, DoctorDetailView
from aplication.core.views.cargo import CargoListView, CargoDetailView, CargoCreateView, CargoDeleteView, CargoUpdateView
from aplication.core.views.empleado import EmpleadoListView, EmpleadoCreateView, EmpleadotUpdateView, EmpleadoDeleteView, EmpleadoDetailView
from aplication.core.views.tipomedicamento import TipoMedicamentoListView, TipomedicamentoCreateView, TipoMedicamentoDeleteView, TipoMedicamentotUpdateView, TipoMedicamentoDetailView
from aplication.core.views.marcamedicamento import MarcaMedicamentoListView, MarcaMedicamentoCreateView, MarcaMedicamentoDeleteView, MarcaMedicamentoUpdateView, MarcaMedicamentoDetailView
from aplication.core.views.medicamento import MedicamentoListView, MedicamentoCreateView, MedicamentoDeleteView, MedicamentoUpdateView, MedicamentoDetailView
from aplication.core.views.examensolicitado import ExamenSolicitadotListView, ExamenSolicitadoCreateView, ExamenSolicitadoDeleteView, ExamenSolicitadoUpdateView, ExamenSolicitadoDetailView
from aplication.core.views.serviciosadd import ServiciosAdicionalesListView, ServiciosAdicionalesCreateView,ServiciosAdicionalesUpdateView,ServiciosAdicionalesDetailView,ServiciosAdicionalesDeleteView
from aplication.core.views.diagnostico import DiagnosticoListView, DiagnosticoCreateView, DiagnosticoDeleteView, DiagnosticoUpdateView, DiagnosticoDetailView
from aplication.core.views.categoriaexamen import *
from aplication.core.views.tipocategoria import *
from aplication.core.views.horarioatencion import *
from aplication.core.views.citamedicam import CitaMedicaCreateView, CitaMedicaDeleteView, CitaMedicaListView, CitaMedicaUpdateView, CitaMedicaFDetailView
from aplication.core.views.auditoria import AuditoriaListView, AuditoriaDetailView
from aplication.core.views.estadistica import  VistaEstadisticas

app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [
  # ruta principal
  path('', HomeTemplateView.as_view(),name='home'),
  # rutas doctores VBF
  # path('doctor_list/', views.doctor_List,name="doctor_list"),
  # path('doctor_create/', views.doctor_create,name="doctor_create"),
  # path('doctor_update/<int:id>/', views.doctor_update,name='doctor_update'),
  # path('doctor_delete/<int:id>/', views.doctor_delete,name='doctor_delete'),
  # rutas doctores VBC
  path('patient_list/',PatientListView.as_view() ,name="patient_list"),
  path('patient_create/', PatientCreateView.as_view(),name="patient_create"),
  path('patient_update/<int:pk>/', PatientUpdateView.as_view(),name='patient_update'),
  path('patient_delete/<int:pk>/', PatientDeleteView.as_view(),name='patient_delete'),
  path('patient_detail/<int:pk>/', PatientDetailView.as_view(),name='patient_detail'),
  
  path('type_list/',BtypeListView.as_view() ,name="type_list"),
  path('type_create/', BtypeCreateView.as_view(),name="type_create"),
  path('type_update/<int:pk>/', BtypeUpdateView.as_view(),name='type_update'),
  path('type_delete/<int:pk>/', BtypeDeleteView.as_view(),name='type_delete'),
  path('type_detail/<int:pk>/', BtypeDetailView.as_view(),name='type_detail'),
  
  path('speciality_list/', SpecialityListView.as_view() ,name="speciality_list"),
  path('speciality_create/', SpecialityCreateView.as_view(), name="speciality_create"),
  path('speciality_update/<int:pk>/', SpecialityUpdateView.as_view(), name='speciality_update'),
  path('speciality_delete/<int:pk>/', SpecialityDeleteView.as_view(), name='speciality_delete'),
  path('speciality_detail/<int:pk>/', SpecialityDetailView.as_view(), name='speciality_detail'),
  
  path('doctor_list/', DoctorListView.as_view(), name="doctor_list"),
  path('doctor_create/', DoctorCreateView.as_view(), name="doctor_create"),
  path('doctor_update/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
  path('doctor_delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),
  path('doctor_detail/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
  
  path('cargo_list/', CargoListView.as_view(), name="cargo_list"),
  path('cargo_create/', CargoCreateView.as_view(), name="cargo_create"),
  path('cargo_update/<int:pk>/', CargoUpdateView.as_view(), name='cargo_update'),
  path('cargo_delete/<int:pk>/', CargoDeleteView.as_view(), name='cargo_delete'),
  path('cargo_detail/<int:pk>/', CargoDetailView.as_view(), name='cargo_detail'),
  
  path('empleado_list/', EmpleadoListView.as_view(), name="empleado_list"),
  path('empleado_create/', EmpleadoCreateView.as_view(), name="empleado_create"),
  path('empleado_update/<int:pk>/',EmpleadotUpdateView.as_view(), name='empleado_update'),
  path('empleado_delete/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado_delete'),
  path('empleado_detail/<int:pk>/', EmpleadoDetailView.as_view(), name='empleado_detail'),
  
  path('tipom_list/', TipoMedicamentoListView.as_view(), name="tipom_list"),
  path('tipom_create/', TipomedicamentoCreateView.as_view(), name="tipom_create"),
  path('tipom_update/<int:pk>/', TipoMedicamentotUpdateView.as_view(), name="tipom_update"),
  path('tipom_delete/<int:pk>/', TipoMedicamentoDeleteView.as_view(), name="tipom_delete"),
  path('tipom_detail/<int:pk>/', TipoMedicamentoDetailView.as_view(), name='tipom_detail'),
  
  path('marca_list/', MarcaMedicamentoListView.as_view(), name="marca_list"),
  path('marca_create/', MarcaMedicamentoCreateView.as_view(), name="marca_create"),
  path('marca_update/<int:pk>/',MarcaMedicamentoUpdateView.as_view(), name='marca_update'),
  path('marca_delete/<int:pk>/', MarcaMedicamentoDeleteView.as_view(), name='marca_delete'),
  path('marca_detail/<int:pk>/', MarcaMedicamentoDetailView.as_view(), name='marca_detail'),
  
  path('medicamento_list/', MedicamentoListView.as_view(), name="medicamento_list"),
  path('medicamento_create/', MedicamentoCreateView.as_view(), name="medicamento_create"),
  path('medicamento_update/<int:pk>/',MedicamentoUpdateView.as_view(), name='medicamento_update'),
  path('medicamento_delete/<int:pk>/',MedicamentoDeleteView.as_view(), name='medicamento_delete'),
  path('medicamento_detail/<int:pk>/', MedicamentoDetailView.as_view(), name='medicamento_detail'),
  
  path('examensolicitado_list/', ExamenSolicitadotListView.as_view(), name="examensolicitado_list"),
  path('examensolicitado_create/', ExamenSolicitadoCreateView.as_view(), name="examensolicitado_create"),
  path('examensolicitado_update/<int:pk>/',ExamenSolicitadoUpdateView.as_view(), name='examensolicitado_update'),
  path('examensolicitado_delete/<int:pk>/', ExamenSolicitadoDeleteView.as_view(), name='examensolicitado_delete'),
  path('examensolicitado_detail/<int:pk>/', ExamenSolicitadoDetailView.as_view(), name='examensolicitado_detail'),
  
  path('servicio_list/', ServiciosAdicionalesListView.as_view(), name="servicio_list"),
  path('servicio_create/', ServiciosAdicionalesCreateView.as_view(), name="servicio_create"),
  path('servicio_update/<int:pk>/',ServiciosAdicionalesUpdateView.as_view(), name='servicio_update'),
  path('servicio_delete/<int:pk>/', ServiciosAdicionalesDeleteView.as_view(), name='servicio_delete'),
  path('servicio_detail/<int:pk>/', ServiciosAdicionalesDetailView.as_view(), name='servicio_detail'),
  
  path('diagnostico_list/', DiagnosticoListView.as_view(), name="diagnostico_list"),
  path('diagnostico_create/', DiagnosticoCreateView.as_view(), name="diagnostico_create"),
  path('diagnostico_update/<int:pk>/',DiagnosticoUpdateView.as_view(), name='diagnostico_update'),
  path('diagnostico_delete/<int:pk>/', DiagnosticoDeleteView.as_view(), name='diagnostico_delete'),
  path('diagnostico_detail/<int:pk>/', DiagnosticoDetailView.as_view(), name='diagnostico_detail'),
  
  path('categoriaexamen_list/', CategoriaExamenListView.as_view(), name="categoriaexamen_list"),
  path('categoriaexamen_create/', CategoriaExamenCreateView.as_view(), name="categoriaexamen_create"),
  path('categoriaexamen_update/<int:pk>/',CategoriaExamenUpdateView.as_view(), name='categoriaexamen_update'),
  path('categoriaexamen_delete/<int:pk>/', CategoriaExamenDeleteView.as_view(), name='categoriaexamen_delete'),
  path('categoriaexamen_detail/<int:pk>/', CategoriaExamenDetailView.as_view(), name='categoriaexamen_detail'),
  
  path('tipocategoria_list/', TipoCategoriaExamenListView.as_view(), name="tipocategoria_list"),
  path('tipocategoria_create/', TipoCategoriaExamenCreateView.as_view(), name="tipocategoria_create"),
  path('tipocategoria_update/<int:pk>/',TipoCategoriaExamenUpdateView.as_view(), name='tipocategoria_update'),
  path('tipocategoria_delete/<int:pk>/', TipoCategoriaExamenDeleteView.as_view(), name='tipocategoria_delete'),
  path('tipocategoria_detail/<int:pk>/', TipoCategoriaExamenDetailView.as_view(), name='tipocategoria_detail'),
  
  path('horarioatencion_list/', HorarioAtencionListView.as_view(), name="horarioatencion_list"),
  path('horarioatencion_create/', HorarioAtencionCreateView.as_view(), name="horarioatencion_create"),
  path('horarioatencion_update/<int:pk>/',HorarioAtencionUpdateView.as_view(), name='horarioatencion_update'),
  path('horarioatencion_delete/<int:pk>/', HorarioAtencionDeleteView.as_view(), name='horarioatencion_delete'),
  path('horarioatencion_detail/<int:pk>/', HorarioAtencionDetailView.as_view(), name='horarioatencion_detail'), 
  
  path('citamedica_list/', CitaMedicaListView.as_view(), name="citamedica_list"),
  path('citamedica_create/', CitaMedicaCreateView.as_view(), name="citamedica_create"),
  path('citamedica_update/<int:pk>/',CitaMedicaUpdateView.as_view(), name='citamedica_update'),
  path('citamedica_delete/<int:pk>/', CitaMedicaDeleteView.as_view(), name='citamedica_delete'),
  path('citamedica_detail/<int:pk>/', CitaMedicaFDetailView.as_view(), name='citamedica_detail'),
  
  path('auditoria_list/', AuditoriaListView.as_view(), name="auditoria_list"),
  path('auditoria_detail/<int:pk>/', AuditoriaDetailView.as_view(), name='auditoria_detail'),
  
  path('attention_list/',AttentionListView.as_view() ,name="attention_list"),
  path('attention_create/', AttentionCreateView.as_view(),name="attention_create"),
  path('attention_update/<int:pk>/', AttentionUpdateView.as_view(),name='attention_update'),
  path('attention_detail/<int:pk>/', AttentionDetailView.as_view(),name='attention_detail'),
  
  path("estadistica/", VistaEstadisticas.as_view(), name="estadistica"),
]