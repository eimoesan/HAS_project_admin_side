from .models import Patient,Doctor,Appointment, Schedule,History
from django import forms
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        #fields = "__all__"     or
        fields = ['doctor_name','doctor_mail','doctor_password','doctor_phoneno','doctor_specialization','doctor_img']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        #fields = "__all__"     or
        fields = ['patient_name','patient_DOB','patient_mail','patient_phoneno','patient_address','patient_password','patient_img']
