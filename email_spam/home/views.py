from django.http import HttpResponse
from django.shortcuts import render
from home.models import *
# Create your views here.

def public_home(request):
    return render (request,'public_pages/public_home.html')

def login(request):
    if 'submit' in request.POST:
        uname = request.POST['username']
        passwd = request.POST['password']
        if Login.objects.filter(username=uname,password=passwd).exists():
            q = Login.objects.get(username=uname, password=passwd)
            request.session['loginid']=q.pk

            if q.usertype=='admin':
                return HttpResponse("<script>alert('Login Success');window.location='admin_home'</script>")
            elif q.usertype=='user':
                f = User.objects.get(LOGIN_id = q.pk)
                if f:
                    request.session['userid'] = f.pk
                    return HttpResponse("<script>alert('Login Success');window.location='public_home'</script>")
            else:
                return HttpResponse("<script>alert('Invalid Login');</script>")

    return render(request,'public_pages/login.html')

def registration(request):
    if 'submit' in request.POST:
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        username = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        photo = request.FILES['photo']
        q = Login(username=username,password=password,usertype='user')
        q.save
        f = User(firstname=fname,lastname=lname,email=email,phone=phone,photo=photo,LOGIN_id=q.pk)
        f.save
        return HttpResponse("<script>alert('Registration Successful');window.location='login'</script>")
    return render(request,'public_pages/registration.html')

def raise_complaint(request):
    return render(request,'public_pages/raise_complaint.html')

def submit_message(request):
    return render(request,'public_pages/submit_message.html')

def view_history(request):
    return render(request, 'public_pages/view_history.html')

def admin_home(request):
    return render(request,'admin_pages/admin_home.html')
