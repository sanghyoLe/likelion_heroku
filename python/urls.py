from django.urls import path
from . import views
urlpatterns = [
    path('',views.python_home,name="python_home"),
    path('python_number/',views.python_number,name="python_number"),
     path('python_list/',views.python_list,name="python_list"),
      path('python_string/',views.python_string,name="python_string"),
       path('python_if/',views.python_if,name="python_if"),
        path('python_for/',views.python_for,name="python_for"),
         path('python_break/',views.python_break,name="python_break"),
          path('python_dictionary/',views.python_dictionary,name="python_dictionary"),
           path('python_exception/',views.python_exception,name="python_exception"),
   path('python_def/',views.python_def,name="python_def"),
]

