from .import views
from django.urls import path, include

urlpatterns = [
    path('', views.retreive_admin,name='retreive_admin'),
    path('retreive_admin_patient_appointments/', views.retreive_admin_patient_appointments,name='retreive_admin_patient_appointments'),
    path('retreive_admin_doctor_schedules/', views.retreive_admin_doctor_schedules,name='retreive_admin_doctor_schedules'),
    path('retreive_admin_doctor/', views.retreive_admin_doctor,name='retreive_admin_doctor'),
    path('update_doctor/<int:id>/',views.update_doctor, name='update_doctor'),
    path('delete_doctor/<int:id>/', views.delete_doctor, name='delete_doctor'),
    path('retreive_admin_schedule_filterby_docname/', views.retreive_admin_schedule_filterby_docname,name='retreive_admin_schedule_filterby_docname'),
    path('retreive_admin_patient_filterby_patname/', views.retreive_admin_patient_filterby_patname,name='retreive_admin_patient_filterby_patname'),
    path('update_patient/<int:id>/',views.update_patient, name='update_patient'),
    path('delete_patient/<int:id>/', views.delete_patient, name='delete_patient'),
    path('retreive_admin_appointment_filterby/', views.retreive_admin_appointment_filterby, name='retreive_admin_appointment_filterby'),

]
