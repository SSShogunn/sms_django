from django.db import models

# Create your models here.

class staff_registration(models.Model):

    staff_number= models.PositiveIntegerField()
    first_name = models.CharField(max_length=100)    
    last_name = models.CharField(max_length=100)
    gender= models.CharField(max_length=100,null=True,blank=True)
    date_of_birth = models.CharField(max_length=1000, null=True)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    faculty_type= models.CharField(max_length=100)
    department = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    date = models.DateField()

    def __str__(self):
        return f'Staff: {self.first_name} {self.last_name}'

class student_registration(models.Model):

    student_number= models.PositiveIntegerField()
    first_name = models.CharField(max_length=100)    
    last_name = models.CharField(max_length=100)
    gender= models.CharField(max_length=100,null=True,blank=True)
    date_of_birth = models.CharField(max_length=1000, null=True)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    course = models.CharField(max_length=100,null=True,blank=True)
    date = models.DateField()
    image = models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'

class event_registration(models.Model): 
    event_name = models.CharField(max_length=100) 
    destination = models.CharField(max_length=100 ,null=True,blank=True)  
    event_date = models.CharField(max_length=100)
    event_contact = models.CharField(max_length=1000)
    event_description = models.CharField(max_length=1000,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    event_thumbnail = models.ImageField(null=True,blank=True,upload_to='images/')    
     
    def __str__(self):
        return self.event_name        

class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()