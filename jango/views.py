from django.shortcuts import render

# Create your views here.

def django_home(request):
    return render(request,'django_home.html')

def django_cheat(request):
    return render(request,'django_cheat.html')

def django_setting(request):
    return render(request,'django_setting.html')

def django_helloworld(request):
    return render(request, 'django_helloworld.html')

    