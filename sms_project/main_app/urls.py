from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path 
from main_app import views

admin.site.site_header = "Learners Admin"
admin.site.site_title = "Learners Admin Portal"
admin.site.index_title = "Welcome to Learners Researcher Portal"

urlpatterns = [
    path("", views.home, name='home'),
    path("home", views.view_event, name='view_event'),

    #student
    path("student_register", views.student_register, name='student_register'),
    path('student_view', views.student_view,name='student_view'),
    path('<int:id>/', views.view_student , name='view_student'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit_student/<int:id>/', views.student_edit, name='student_edit'),

    #staff
    path("staff_register", views.staff_register , name='staff_register'),
    path('staff_view', views.staff_view,name='staff_view'),
    path('<int:id>/', views.view_staff , name='view_staff'),
    path('delete/<int:id>/', views.staff_delete, name='staff_delete'),
    path('edit_staff/<int:id>/', views.staff_edit, name='staff_edit'),

    #events
    path("event_register", views.event_register, name='event_register'),

    #login
    path('login/', views.login_view, name='login_view'),
    path('logout_user/', views.logout_user, name="logout_user"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






