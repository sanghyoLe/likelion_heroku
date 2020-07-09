from django.urls import path
from . import views

urlpatterns = [
    path('',views.django_home,name="django_home"),
    path('cheat/',views.django_cheat,name="django_cheat"),
    path('setting/',views.django_setting,name="django_setting"),
    path('helloworld/',views.django_helloworld,name="django_helloworld"),

]

