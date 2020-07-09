from django.shortcuts import render

# Create your views here.

def python_home(request):
    return render(request,'python_home.html')

def python_number(request):
    return render(request,'python_number.html')

def python_list(request):
    return render(request,'python_list.html')

def python_string(request):
    return render(request,'python_string.html')

def python_if(request):
    return render(request,'python_if.html')

def python_for(request):
    return render(request,'python_for.html')

def python_break(request):
    return render(request,'python_break.html')

def python_dictionary(request):
    return render(request,'python_dictionary.html')

def python_exception(request):
    return render(request,'python_exception.html')

def python_def(request):
    return render(request,'python_def.html')
