from django.shortcuts import render

# Create your views here.

def user_master(request):
    return render(request,'user/master.html')

def user_home(request):
    return render(request,'user/home.html')

def user_about(request):
    return render(request,'user/about.html')

def user_contact(request):
    return render(request,'user/contact.html')

