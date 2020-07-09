from django.shortcuts import render

# Create your views here.

def git_home(request):
    return render(request,'git_home.html')

def git_base(request):
    return render(request,'git_base.html')

def git_deep(request):
    return render(request,'git_deep.html')