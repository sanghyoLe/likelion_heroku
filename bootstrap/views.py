from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def bootstrap(request):
    return render(request,'Gaeyo.html')

def ui(request):
    return render(request,'ui.html')

def GaeyoBase(request):
    return render(request,'Gaeyo_base.html')

def use_ui(request):
    return render(request,'useui.html')

def make_navbar(request):
    return render(request,'make_navbar.html')

def breakpoint(request):
    return render(request,'breakpoint.html')

def dark_light(request):
    return render(request,'dark_light.html')

def grid(request):
    return render(request,'grid.html')

def row_col(request):
    return render(request, 'row_col.html')

def column(request):
    return render(request, 'column.html')

def flex_desine(request):
 return render(request, 'flex_desine.html')
 
def bootstrap_custom(request):
    return render(request, 'bootstrap_custom.html')

def notyet(request):
    return render(request,'notyet.html')

 