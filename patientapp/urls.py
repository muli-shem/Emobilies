from django.contrib import admin
from django.urls import path
from patientapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name= 'home'),
    path('about/',views.about ,name='about'),
    path('contact/submit/', views.handle_contact_form ,name='contact_submit'),
    path('service/', views.service ,name='service'),


]
