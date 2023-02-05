from django.contrib import admin
from .models import staff_registration, student_registration, event_registration
# Register your models here.

admin.site.register(staff_registration)
admin.site.register(student_registration)
admin.site.register(event_registration )
