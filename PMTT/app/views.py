from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='pages/login')
def Base(request):
    return render(request, 'pages/base.html', {})

def dashboard(request):
    return render(request, 'pages/dashboard.html', {})     

def testing(request):
    return render(request, 'pages/testing.html', {})   

def allprojects(request):
    return render(request, 'pages/allprojects.html', {})

def conference(request):
    return render(request, 'pages/conference.html', {})

def createproject(request):
    return render(request, 'pages/createproject.html', {})

def calendar(request):
    return render(request, 'pages/calendar.html', {})

def cost(request):
    return render(request, 'pages/cost.html', {})

def login(request):
    context = ()
    return render(request, 'pages/login.html', {})

def profile(request):
    return render(request, 'pages/profile.html', {})

def reportcreation(request):
    return render(request, 'pages/reportcreation.html', {})

def risk(request):
    return render(request, 'pages/risk.html', {})

def skillgap(request):
    return render(request, 'pages/skillgap.html', {})

def task(request):
    return render(request, 'pages/task.html', {})

def datavisual(request):
    return render(request, 'pages/datavisual.html', {})

def discussion(request):
    return render(request, 'pages/discussion.html', {})
