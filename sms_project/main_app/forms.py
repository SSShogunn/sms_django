from django import forms
from .models import student_registration,staff_registration,event_registration

class StudentForm (forms.ModelForm):
    class Meta:
        model = student_registration
        fields = ['student_number', 'first_name', 'last_name','gender','date_of_birth','phone','email','password','course','image']
        labels = {
            'student_number' : 'Student Number',
            'first_name' : 'First Name', 
            'last_name': 'Last Name', 
            'gender' : 'Gender',
            'date_of_birth' : 'DOB',
            'phone': 'Phone Number',
            'email' : "Email",
            'password' : "Password",
            'course' : "Course",
            'image' : "Image"
        }
        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'form-control'}), 
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
    }
 
class StaffForm (forms.ModelForm):
    class Meta:
        model = staff_registration      
        fields = ['staff_number', 'first_name', 'last_name','gender','date_of_birth','phone','email','password','faculty_type','department','image']
        labels = {
            'staff_number' : 'Student Number',
            'first_name' : 'First Name', 
            'last_name': 'Last Name', 
            'gender' : 'Gender',
            'date_of_birth' : 'DOB',
            'phone': 'Phone Number',
            'email' : "Email",
            'password' : "Password",
            'faculty_type' : "Faculty type",
            'department' : "Department",
            'image' : "Image"
        }
        widgets = {
            'staff_number': forms.NumberInput(attrs={'class': 'form-control'}), 
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'faculty_type': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
    }

