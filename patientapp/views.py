from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, template_name='index.html')

def about(request):
    return render(request, template_name='about.html')
def handle_contact_form(request):
    return render(request,template_name='contact.html' )
def service(request):
    return render(request, template_name="Service.html")

