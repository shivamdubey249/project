from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from ExamApp.forms import SignupForm
from django.contrib.auth.models import User
# Create your views here.
def homeview(request):
    return render(request,"ExamApp/home.html")

@login_required
def cppview(request):
    return render(request,"ExamApp/cpp.html")

def javaview(request):
    return render(request,"ExamApp/java.html")


def pythonview(request):
    return render(request,"ExamApp/python.html")

def signupview(request):
    if request.method=='GET':
        sform=SignupForm()
        return render(request,"ExamApp/signup.html",{'sform':sform})
    if request.method=='POST':
            sform=SignupForm(request.POST)
            user=sform.save()
            user.set_password(user.password)
            user.save()
            return render(request,"ExamApp/success.html",{'msg':'Registration Success...'})
