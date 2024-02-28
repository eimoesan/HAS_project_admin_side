from django.db import models

# Create your models here.
class Doctor(models.Model):
    doctor_id = models.BigAutoField(primary_key=True, serialize=False)
    doctor_name = models.CharField(max_length=100)
    doctor_mail = models.EmailField()
    doctor_password = models.CharField(max_length=50)
    doctor_phoneno = models.BigIntegerField()
    doctor_specialization = models.CharField(max_length=100)
    doctor_img = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.doctor_name

class History(models.Model):
    history_id = models.BigAutoField(primary_key=True, serialize=False)
    status = models.CharField(max_length=100)
    def __str__(self):
        return self.status

class Patient(models.Model):
    patient_id = models.BigAutoField(primary_key=True, serialize=False)
    patient_name = models.CharField(max_length=100)
    patient_DOB = models.DateField()
    patient_mail = models.EmailField()
    patient_phoneno = models.BigIntegerField()
    patient_address = models.CharField(max_length=400)
    patient_password = models.CharField(max_length=50)
    patient_img = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.patient_name

class Appointment(models.Model):
    appointment_id = models.BigAutoField(primary_key=True, serialize=False)
    doctor_id = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE)
    history_id = models.ForeignKey(History,on_delete=models.CASCADE)
    appoint_date = models.DateField()
    appoint_start_time = models.TimeField()
    appoint_end_time = models.TimeField()
    token = models.PositiveIntegerField()
    def __str__(self):
        return str(self.token)

class Schedule(models.Model):
    schedule_id = models.BigAutoField(primary_key=True, serialize=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    schedule_date = models.DateField()
    schedule_start_time = models.TimeField()
    schedule_end_time = models.TimeField()
    maxpatient = models.PositiveIntegerField()
    def __str__(self):
        return str(self.schedule_date)

class Admin(models.Model):
    email = models.EmailField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    img = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.email