from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from .models import Patient,Doctor,Appointment, Schedule,History
from .forms import DoctorForm,PatientForm
#admin select to show patient or doctor
def retreive_admin(request):
    patient_count = Appointment.objects.filter(appoint_date=timezone.now().date()).count()
    doctor_count = Schedule.objects.filter(schedule_date=timezone.now().date()).count()
    count = (patient_count,doctor_count)
    print(count)
    return render(request, 'hospital_appointment_system/admin_dashboard.html', {'count':count})

#admin dashboard show patient's appointments
def retreive_admin_patient_appointments(request):
    print('in retreive_admin_patient_appointments')
    patient_count = Appointment.objects.filter(appoint_date=timezone.now().date()).count()
    doctor_count = Schedule.objects.filter(schedule_date=timezone.now().date()).count()
    count = (patient_count, doctor_count)
    appointment_table = Appointment.objects.filter(appoint_date=timezone.now().date())
    # appoint_start_time = Appointment.objects.values_list('appoint_start_time')
    # appointment_end_time=Appointment.objects.values_list('appoint_end_time')
    # appointment_table = (appoint_start_time,appointment_end_time)
    print(appointment_table)
    #DoctorName	PatientName	AppointStartTime	AppointEndTime
    return render(request, 'hospital_appointment_system/admin_appointment_table.html', {'appointment_table':appointment_table,'count':count})

#admin dashboard show doctor's schedules
def retreive_admin_doctor_schedules(request):
    print('in retreive_admin_doctor_schedules')
    patient_count = Appointment.objects.filter(appoint_date=timezone.now().date()).count()
    doctor_count = Schedule.objects.filter(schedule_date=timezone.now().date()).count()
    count = (patient_count, doctor_count)
    # result = Schedule.objects.select_related('doctor_id').all()
    result = Schedule.objects.filter(schedule_date=timezone.now().date())
    print(result.query)
    return render(request, 'hospital_appointment_system/admin_schedule_table.html', {'count':count,'result':result})

#admin show doctor
def retreive_admin_doctor(request):
    print('in retreive_admin_doctor')
    doctor_table = Doctor.objects.all()
    print(doctor_table)
    return render(request, 'hospital_appointment_system/admin_doctor_table.html', {'doctor_table':doctor_table})

def update_doctor(request, id):
    print(id)
    data = Doctor.objects.get(doctor_id=id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = DoctorForm(instance=data)
    return render(request,'hospital_appointment_system/update_doctorForm.html',{'form':form})
#delete
def delete_doctor(request, id):
    Doctor.objects.get(doctor_id=id).delete()
    return HttpResponseRedirect('/')

def retreive_admin_schedule_filterby_docname(request):
    print('in retreive_admin_schedule_filterby_docname')
    schedule_table = Schedule.objects.all()
    doctor_name_query = request.GET.get('doctor_name')
    print(doctor_name_query)
    message = ""
    if doctor_name_query != '' and doctor_name_query is not None:
        schedule_table = schedule_table.filter(doctor_id__doctor_name__icontains=doctor_name_query)
        print(schedule_table)
        print(schedule_table.query)
        message = "No of results found for " + "'" + str(doctor_name_query) + "'" +" : "+ str(schedule_table.count())
    return render(request, 'hospital_appointment_system/admin_schedule_filterby_docname.html', {'schedule_table':schedule_table,'message':message})

def retreive_admin_patient_filterby_patname(request):
    print('in retreive_admin_patient_filterby_patname')
    patient_table = Patient.objects.all()
    patient_name_query = request.GET.get('patient_name')
    print(patient_name_query)
    message = ""
    if patient_name_query != '' and patient_name_query is not None:
        patient_table = patient_table.filter(patient_name__icontains=patient_name_query)
        print(patient_table)
        print(patient_table.query)
        message = "No of results found for " + "'" + str(patient_name_query) + "'" +" : "+ str(patient_table.count())
    return render(request, 'hospital_appointment_system/admin_patient_table.html', {'patient_table':patient_table,'message':message})

def update_patient(request, id):
    print(id)
    data = Patient.objects.get(patient_id=id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/retreive_admin_patient_filterby_patname')
    else:
        form = PatientForm(instance=data)
    return render(request,'hospital_appointment_system/update_patientForm.html',{'form':form})
#delete
def delete_patient(request, id):
    Patient.objects.get(patient_id=id).delete()
    return HttpResponseRedirect('/retreive_admin_patient_filterby_patname')

def retreive_admin_appointment_filterby(request):
    print('in retreive_admin_appointment_filterby')
    appointment_table = Appointment.objects.all()
    print(appointment_table.query)
    patient_name_query = request.GET.get('patient_name')
    doctor_name_query = request.GET.get('doctor_name')
    from_date_query = request.GET.get('from')
    to_date_query = request.GET.get('to')
    print(from_date_query, to_date_query)
    message = ""
    if (from_date_query == '' or from_date_query is None) or (to_date_query == '' or to_date_query is None):
        if (patient_name_query != '' and patient_name_query is not None) :
            appointment_table = Appointment.objects.filter(patient_id__patient_name__icontains=patient_name_query)
            print("one ",appointment_table.query)
            message = "Search results for " + "'" + str(patient_name_query) + "'" + " : " + str(appointment_table.count())
        if (doctor_name_query != '' and doctor_name_query is not None) :
            appointment_table = appointment_table.filter(doctor_id__doctor_name__icontains=doctor_name_query)
            print("two ",appointment_table.query)
            message = "Search results for " + "'" + str(doctor_name_query) + "'" + " : " + str(appointment_table.count())
        if (patient_name_query != '' and patient_name_query is not None) and (doctor_name_query != '' and doctor_name_query is not None):
            appointment_table = Appointment.objects.filter(patient_id__patient_name__icontains=patient_name_query, doctor_id__doctor_name__icontains=doctor_name_query)
            print("three ",appointment_table.query)
            message = "Search results for patient name " + "'" + str(patient_name_query) + "'" +" and doctor name "+ "'" + str(doctor_name_query) + "'" + " : " + str(appointment_table.count())
    if (from_date_query != '' and from_date_query is not None) and (to_date_query != '' and to_date_query is not None):
        if ((patient_name_query != '' and patient_name_query is not None) and (doctor_name_query != '' and doctor_name_query is not None)):
            appointment_table = Appointment.objects.filter(appoint_date__range=(from_date_query, to_date_query),patient_id__patient_name__icontains=patient_name_query,doctor_id__doctor_name__icontains=doctor_name_query)
            message = "Search results for patient name " + "'" + str(patient_name_query) + "'" + ", Doctor name " + "'" + str(doctor_name_query) + "'" + " and appointment dates between" + "'" + str(from_date_query) + "'" +" and "+ "'" + str(to_date_query) + "'" + " : " + str(appointment_table.count())
            print("four ", appointment_table.query)
        elif (doctor_name_query != '' and doctor_name_query is not None) :
            appointment_table = appointment_table.filter(appoint_date__range=(from_date_query, to_date_query),doctor_id__doctor_name__icontains=doctor_name_query)
            print("five ",appointment_table.query)
            message = "Search results for " + "'" + str(doctor_name_query) + "'" + " and appointment dates between" + "'" + str(from_date_query) + "'" +" and "+ "'" + str(to_date_query) + "'" + " : " + str(appointment_table.count())
        elif (patient_name_query != '' and patient_name_query is not None) :
            appointment_table = Appointment.objects.filter(appoint_date__range=(from_date_query, to_date_query),patient_id__patient_name__icontains=patient_name_query)
            print("six ",appointment_table.query)
            message = "Search results for " + "'" + str(patient_name_query) + "'" + " and appointment dates between" + "'" + str(from_date_query) + "'" +" and "+ "'" + str(to_date_query) + "'" + " : " + str(appointment_table.count())
        else:
            appointment_table = Appointment.objects.filter(appoint_date__range=(from_date_query, to_date_query))
            message = "Search results for appointment dates between" + "'" + str(from_date_query) + "'" +" and "+ "'" + str(to_date_query) + "'" + " : " + str(appointment_table.count())
            print("seven ", appointment_table.query)
    return render(request, 'hospital_appointment_system/admin_appointment_filterby.html', {'appointment_table': appointment_table, 'message':message})
