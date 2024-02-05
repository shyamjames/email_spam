from django.shortcuts import render

# Create your views here.

def public_home(request):
    return render (request,'public_pages/public_home.html')