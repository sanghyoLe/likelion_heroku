from django.urls import path
from . import views
urlpatterns = [
    path('',views.git_home,name="git_home"),
    path('base/',views.git_base,name="git_base"),
    path('deep/',views.git_deep,name="git_deep"),
]

