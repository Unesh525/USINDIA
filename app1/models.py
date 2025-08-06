from django.db import models

# Create your models here.
class admindata(models.Model):
    name = models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    email=models. CharField (max_length=100,primary_key=True)
    def __str__(self): #python 2 def __unicode__(self):
        return self.email

class logindata(models.Model):
    email=models. CharField (max_length=100,primary_key=True)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100)
    def __str__(self):
        return self.email

class userdata(models.Model):
    name = models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models. CharField (max_length=100,primary_key=True)
    def __str__(self): #python 2 def __unicode__(self):
        return self.email



class PhishingLink(models.Model):
    email = models.EmailField()
    unique_code = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email

class PhishedData(models.Model):
    phishing_link = models.ForeignKey(PhishingLink, on_delete=models.CASCADE)
    entered_username = models.CharField(max_length=200)
    entered_password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.entered_username}(From:{self.phishing_link.email})"


