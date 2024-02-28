from django.contrib import admin

from .models import History, Appointment, Doctor, Admin, Patient, Schedule

# Register your models here.
admin.site.register(History)
admin.site.register(Appointment)
admin.site.register(Doctor)
admin.site.register(Admin)
admin.site.register(Patient)
admin.site.register(Schedule)
