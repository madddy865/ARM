from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from app2.models import *
from .import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from app2.models import StudentPassword
from django.db import models


def StdLogin_view(request):
    if request.method == 'POST':
        # form =forms.LoginForm
        # if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        try:
          userA=StudentPassword.objects.get(username=username)
        except ObjectDoesNotExist:
            return HttpResponse("Invalid login credentials")
        if userA.password==password:
            return redirect('home.html')
        else:
            return HttpResponse("Username or password is incorrect")
    else:
        return render(request,'studentLogin.html')        
    # return render(request,'studentLogin.html')  




def registration_view(request):
    form=forms.RegistrationForm
    if request.method=="POST":
        form=forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'Registration.html',{'form':form})


def home_view(request):
    return render(request,'home.html')


def attendance_view(request):
    return render( request,'attendance.html')


def about_view(request):
    return render( request,'about.html')

def coursedetails_view(request):
    return render( request,'coursedetails.html')

def Student_details_view(request):
    Student_list=Ignitz.objects.all()
    my_dict={'Student_list':Student_list}
    return render(request, 'student_details.html',context=my_dict)

def Attendance_details_view(request):
    Attendance_list=Attendance.objects.all()
    my_dict={'Attendance_list':Attendance_list}
    return render(request, 'Attendance_details.html',context=my_dict)


def Attendance_view(request):
    form=forms.AttendanceForm
    if request.method=="POST":
        form=forms.AttendanceForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'attendance.html',{'form':form})


def Login_view(request):
    if request.method == 'POST':
        # form =forms.LoginForm
        # if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('loginmain')
        else:
                # return redirect('loginmain')
            return HttpResponse("Invalid login credentials")
    return render(request,'login.html')
@login_required
def loginmain_view(request):
    return render(request,'loginmain.html')

def StudentPassword(request):
    form=forms.StdPasswordForm
    if request.method=="POST":
        form=forms.StdPasswordForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'StdCreatePassword.html',{'form':form})

 
@login_required
def loginmain_view(request):
    return render(request,'loginmain.html')

def signupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("password should be same")
        else:  
            signupPage.save(commit=True)
    return render(request,'StdCreatePassword.html')