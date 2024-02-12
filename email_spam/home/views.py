from django.http import HttpResponse
from django.shortcuts import render, redirect
from home.models import *
import datetime
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
                    request.session['user_id'] = f.pk
                    return HttpResponse("<script>alert('Login Success');window.location='user_home'</script>")
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
        q.save()
        f = User(firstname=fname,lastname=lname,email=email,phone=phone,photo=photo,LOGIN_id=q.pk)
        f.save()    
        return HttpResponse("<script>alert('Registration Successful');window.location='login'</script>")
    return render(request,'public_pages/registration.html')

def raise_complaint(request):
    date = datetime.datetime.now()
    if 'submit' in request.POST:
        subject = request.POST['dropdown_selection']
        complaint = request.POST['complaint_text']
        q = Complaint(complaint_text=complaint,subject=subject,date_time=date,USER_id=request.session['user_id'],response='pending')
        q.save()
    return render(request,'public_pages/raise_complaint.html')

def submit_message(request):
    date = datetime.datetime.now()
    q1 = Message.objects.filter(USER_id=request.session['user_id'])
    if 'submit' in request.POST:
        message = request.POST['message_text']
        q = Message(USER_id=request.session['user_id'],message_text=message,date_time=date)
        q.save()
    return render(request,'public_pages/submit_message.html',{'q1':q1})

def view_history(request):
    q1 = Message.objects.filter(USER_id=request.session['user_id'])     
    return render(request, 'public_pages/submit_message.html',{'q1':q1})

def update_message(request,id):
    q1 = Message.objects.filter(USER_id=request.session['user_id'])
    q = Message.objects.get(id=id)
    if 'update' in request.POST:
        message = request.POST['message_text']
        q.message_text=message
        q.save()
        return HttpResponse("<script>alert('updated Successful');window.location='/submit_message'</script>")
    return render(request,'public_pages/submit_message.html',{'q':q,'q1':q1 })

def delete_message(request,id):
    q = Message.objects.get(id=id)
    q.delete()
    return HttpResponse("<script>alert('Deletion Successful');window.location='/submit_message'</script>")
    

def admin_home(request):
    return render(request,'admin_pages/admin_home.html')

def user_home(request):
    return render(request,'public_pages/user_home.html')

def password_reset(request):
    return render(request,'public_pages/password_reset.html')

def feedback(request):
    date = datetime.datetime.now()
    if 'submit' in request.POST:
        feedback = request.POST['feedback_text']
        q = Feedback(USER_id=request.session['user_id'],feedback_text=feedback,date_time=date)
        q.save()
    return render(request,'public_pages/feedback.html')

def user_header(request):
    return render(request,'public_pages/user_header.html')

def logout(request):
    del request.session['user_id']
    request.session.flush()
    return redirect('login')