from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
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
    q1 = Complaint.objects.filter(USER_id=request.session['user_id'])
    date = datetime.datetime.now()
    if 'submit' in request.POST:
        subject = request.POST['subject']
        complaint = request.POST['complaint_text']
        q = Complaint(complaint_text=complaint,subject=subject,date_time=date,USER_id=request.session['user_id'],response='pending')
        q.save()
        return HttpResponse("<script>alert('Complaint added succesfully');window.location='/raise_complaint'</script>")
    return render(request,'public_pages/raise_complaint.html',{'q1':q1})

# def view_complaints(request):
#     q1 = Complaint.objects.filter(USER_id=request.session['user_id'])
#     return render(request,'public_pages/raise_complaint.html',{'q1':q1})

# def submit_message(request):
#     date = datetime.datetime.now()
#     q1 = Message.objects.filter(USER_id=request.session['user_id'])
#     if 'submit' in request.POST:
#         message = request.POST['message_text']
#         q = Message(USER_id=request.session['user_id'],message_text=message,date_time=date)
#         q.save()
    
#     return render(request,'public_pages/submit_message.html',{'q1':q1})

def submit_message(request):
    date = datetime.datetime.now()
    q1 = Message.objects.filter(USER_id=request.session['user_id'])
    if 'submit' in request.POST:
        text = request.POST['message_text']

        from textblob.classifiers import NaiveBayesClassifier
        import pandas

        var = r"C:\Users\shyam\Desktop\email_spam_recognition\email_spam\static\spamham.csv"

        pd = pandas.read_csv(var)

        x = pd.values[:1000, :]

        train = []

        for i in x:
            train.append((i[1], i[0]))

        a = NaiveBayesClassifier(train)

        s = a.classify(text)
        da = date
        print(s)
        if Message.objects.filter(USER_id=request.session['user_id'], is_spam=s, message_text=text).exists():
            pass
        else:
            Fa = Message()
            Fa.message_text = text
            Fa.date_time = da
            Fa.USER_id = request.session['user_id']
            Fa.is_spam = s
            Fa.save()
        

    return render(request, 'public_pages/submit_message.html', {'q1': q1})

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

# def view_user(request):
#     data=User.objects.all()
#     return render(request,'admin_pages/viewuser.html',{'data':data})

def admin_user_delete(request, id):
    q = User.objects.get(id=id)
    q.delete()
    return HttpResponse("<script>alert('Deletion Successful');window.location='/admin_home'</script>")
   


def admin_home(request):
    data = User.objects.all()
    return render(request,'admin_pages/admin_home.html',{'data':data})

def admin_header(request):
    return render(request,'admin_pages/admin_header.html')

def user_home(request):
    return render(request,'public_pages/user_home.html')

def admin_footer(request):
    return render(request,'admin_pages/admin_footer.html')

def user_footer(request):
    return render(request,'public_pages/user_footer.html')

def feedback(request):
    date = datetime.datetime.now()
    if 'submit' in request.POST:
        feedback = request.POST['feedback_text']
        q = Feedback(USER_id=request.session['user_id'],feedback_text=feedback,date_time=date)
        q.save()
        return HttpResponse("<script>alert('Feedback Success');window.location='feedback'</script>")
    return render(request,'public_pages/feedback.html')

def user_header(request):
    return render(request,'public_pages/user_header.html')

def logout(request):
    # del request.session['user_id']
    request.session.flush()
    return HttpResponse("<script>window.location='/login'</script>")

def admin_complaints(request):
    q1 = Complaint.objects.all().order_by('-date_time')
    return render(request,'admin_pages/admin_complaints.html',{'q1':q1})

def admin_resolve_complaint(request,id):
    q = Complaint.objects.get(id=id)
    if 'resolve' in request.POST:
        response = request.POST['response']
        q.response = response
        q.save()
        return HttpResponse("<script>alert('Resolve Success');window.location='/admin_complaints'</script>")
    return render(request,'admin_pages/admin_resolve_complaint.html')

def admin_complaint_delete(request, id):
    q = Complaint.objects.get(id=id)
    q.delete()
    return HttpResponse("<script>alert('Deletion Successful');window.location='/admin_complaints'</script>")

def admin_feedback(request):
    q1 = Feedback.objects.all
    return render(request,'admin_pages/admin_feedback.html',{'q1':q1})






# ---------------------------------------android--------------------------------------

def login_and(request):
    username = request.POST['username']
    password = request.POST['password']
    if Login.objects.filter(username=username,password=password).exists():
        q = Login.objects.get(username=username,password=password)
        lid = q.pk
        if q.usertype == 'user':
            m = User.objects.get(LOGIN_id=lid)
            if m:
                uid = m.pk
                return JsonResponse({'status':'ok','lid':lid,'uid':uid})
            else:
                return JsonResponse({'status':'no'})
    else:
        return JsonResponse({'status':'no'})
    

def signup_and(request):
    firstname = request.POST['fname']
    lastname = request.POST['lname']
    username = request.POST['username']
    email = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['password']
    photo = request.POST['photo']
    import base64

    b=base64.b64decode(photo)
    import datetime
    d=datetime.datetime.now().strftime("%y%m%d%H%M%S")+".jpg"
    with open("C:\\Users\\shyam\\Desktop\\email_spam_recognition\\email_spam\\static\\user\\"+d,"wb") as f:
        f.write(b)
        f.close()
    q = Login(username = username,password = password,usertype='user')
    q.save()
    path="/static/user/"+d
    r = User(firstname=firstname,lastname=lastname,email=email,phone=phone,photo=path,LOGIN_id=q.pk)
    r.save()
    return JsonResponse({'status':'ok'})


def feeedback_and(request):
    feedback = request.POST['feedback']
    lid = request.POST['lid']
    user=User.objects.get(LOGIN_id=lid)
    da=datetime.datetime.now()
    Fa=Feedback()
    Fa.feedback_text=feedback
    Fa.date_time=da
    Fa.USER=user
    Fa.save()
    return JsonResponse({'status':'ok'})
   
def complaint_and(request):
    feedback = request.POST['complaint']
    subject = request.POST['subject']
    lid = request.POST['lid']
    user=User.objects.get(LOGIN_id=lid)
    da=datetime.datetime.now()
    Fa=Complaint()
    Fa.complaint_text=feedback
    Fa.date_time=da
    Fa.USER=user
    Fa.response="Pending"
    Fa.subject=subject
    Fa.save()
    return JsonResponse({'status':'ok'})

def reply_and(request):
    lid = request.POST['lid']
    user=User.objects.get(LOGIN_id=lid)
    data=[]
    cc=Complaint.objects.filter(USER=user)
    for i in cc:
        data.append({"complaint_id":i.id,"complaint":i.complaint_text,"status":i.subject,"date":i.date_time,"reply":i.response,'user_id':i.USER.id})
    return JsonResponse({'status':'ok',"data":data})

def predict_and(request):
    lid = request.POST['lid']
    text = request.POST['text']
    print(text)
    user=User.objects.get(LOGIN_id=lid)
    from textblob.classifiers import NaiveBayesClassifier
    import pandas

    var = r"C:\Users\shyam\Desktop\email_spam_recognition\email_spam\static\spamham.csv"

    pd = pandas.read_csv(var)

    x = pd.values[:1000, :]

    train = []

    for i in x:
        train.append((i[1], i[0]))

    a = NaiveBayesClassifier(train)

    s = a.classify(text)
    da=datetime.datetime.now()
    print(s)
    if Message.objects.filter(USER=user,is_spam=s,message_text=text).exists():
        pass
    else:
        Fa=Message()
        Fa.message_text=text
        Fa.date_time=da
        Fa.USER=user
        Fa.is_spam=s
        Fa.save()
    return JsonResponse({'status':'ok',"result":"This is likely to be "+ s})



def msgs_and(request):
    lid = request.POST['lid']
    user=User.objects.get(LOGIN_id=lid)
    data=[]
    cc=Message.objects.filter(USER=user)
    for i in cc:
        data.append({"complaint_id":i.id,"complaint":i.message_text,"status":i.is_spam,"date":i.date_time,"reply":i.is_spam,'user_id':i.USER.id})
    return JsonResponse({'status':'ok',"data":data})