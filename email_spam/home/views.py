from django.shortcuts import render

# Create your views here.

def public_home(request):
    return render (request,'public_pages/public_home.html')

def login(request):
    return render(request,'public_pages/login.html')

def registration(request):
    return render(request,'public_pages/registration.html')

def raise_complaint(request):
    return render(request,'public_pages/raise_complaint.html')

def submit_message(request):
    return render(request,'public_pages/submit_message.html')