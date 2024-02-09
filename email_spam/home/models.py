from django.db import models

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=16)
    usertype = models.CharField(max_length=5)

class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='static/user')

class Message(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    message_text = models.CharField(max_length=2000)
    date_time = models.CharField(max_length=255)
    is_spam = models.CharField(max_length=10,default='pending')

class Feedback(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    feedback_text = models.CharField(max_length=2000)
    date_time = models.CharField(max_length=255)

class Complaint(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    complaint_text = models.CharField(max_length=2000)
    response = models.CharField(max_length=2000)
    date_time = models.CharField(max_length=255,default='pending')
    subject = models.CharField(max_length=255,default='pending')