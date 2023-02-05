from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import student_registration, event_registration, staff_registration
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
# Create your views here.

def home(request):
    return render(request , 'home.html')

def student_register(request):
    if request.method == "POST":
        student_number = request.POST.get('student_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        course = request.POST.get('course')
        image = request.FILES.get('image')

        student_info = student_registration(
            student_number=student_number,
            first_name=first_name,
            last_name = last_name,
            gender=gender, 
            date_of_birth=date_of_birth, 
            phone=phone, 
            email=email, 
            password=password,
            course=course,image=image,
            date=datetime.today()
        )
        student_info.save()
        messages.success(request, "Student Added Successfully!")  

    return render(request , 'add_student.html')


def staff_register(request):
    if request.method == "POST":
        staff_number=request.POST.get('staff_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        image = request.FILES.get('image')
        faculty_type = request.POST.get('faculty_type')
        department = request.POST.get('department')

        staff_info = staff_registration(
            staff_number=staff_number,
            first_name=first_name,
            last_name = last_name,
            gender=gender, 
            date_of_birth=date_of_birth, 
            phone=phone, email=email, 
            password=password,image=image, 
            faculty_type=faculty_type, 
            department=department,
            date=datetime.today()
            )
        staff_info.save()

        messages.success(request, "Staff Added Successfully!")  

    return render(request , 'add_staff.html')


def event_register(request):
    if request.method == "POST":
        event_name = request.POST.get('event_name') 
        destination = request.POST.get('destination')  
        event_contact = request.POST.get('event_contact')
        event_description = request.POST.get('event_description') 
        event_date = request.POST.get('event_date')  
        event_thumbnail = request.FILES.get('event_thumbnail')  

        event_info = event_registration(
            event_name=event_name,
            destination=destination,
            event_contact=event_contact, 
            event_date=event_date,
            event_description=event_description, 
            event_thumbnail=event_thumbnail)
        event_info.save()

        messages.success(request, "Event Added Successfully!") 

    return render(request , 'add_event.html')  


def student_view(request):
    return render(request, 'view_student.html',{
        'students' : student_registration.objects.all()
    })

def view_student(request, id):
    student = student_registration.objects.get(pk=id)
    return HttpResponseRedirect(reverse('student_view'))


def student_edit(request, id):
    if request.method == "POST":
       student = student_registration.objects.get(pk=id) 
       form = StudentForm(request.POST, instance=student)
       if form.is_valid():
        form.save()
        return render(request, 'edit_student.html', {
            'form': form,
            'success': True
        })
    else:
        student = student_registration.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html',{
        'form':form
    })
    
def delete(request, id):
    if request.method == 'POST':
        student = student_registration.objects.get(pk=id)
        student.delete()
        return HttpResponseRedirect(reverse('student_view'))    

def staff_view(request):
    return render(request, 'view_staff.html',{
        "staffs" : staff_registration.objects.all()
    })

def view_staff (request, id):
    staff = staff_registration.objects.get(pk=id)    
    return HttpResponseRedirect(reverse('staff_view'))

def staff_edit(request, id):
    if request.method == "POST":
        staff = staff_registration.objects.get(pk = id)
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return render(request, 'edit_staff.html',{
                'form' : form,
                'success' : True
            })
    else:
            staff = staff_registration.objects.get(pk = id)
            form = StaffForm(instance=staff)
    return render(request, 'edit_staff.html',{
        'form' : form
    })   


def staff_delete(request,  id):
    if request.method == 'POST':
        staff = staff_registration.objects.get(pk = id)
        staff.delete()
        return HttpResponseRedirect(reverse('staff_view'))

def view_event(request):
    return render( request, 'home.html',{
        "events" : event_registration.objects.all()
    })





































































def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

    
