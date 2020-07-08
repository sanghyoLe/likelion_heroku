"""page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import bootstrap.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',bootstrap.views.home,name="home"),
    path('notyet/',bootstrap.views.notyet,name="notyet"),
    path('bootstarp/',bootstrap.views.bootstrap,name="bootstrap"),
    path('bootstrap/ui',bootstrap.views.ui,name="ui"),
    path('bootstrap/use_ui',bootstrap.views.use_ui,name="use_ui"),
    path('bootstrap/make_navbar',bootstrap.views.make_navbar,name="make_navbar"),
    path('bootstrap/breakpoint',bootstrap.views.breakpoint,name="breakpoint"),
    path('bootstrap/dark_light',bootstrap.views.dark_light,name="dark_light"),
    path('bootstrap/grid',bootstrap.views.grid,name="grid"),
    path('bootstrap/row_col',bootstrap.views.row_col,name="row_col"),
    path('boostrap/column',bootstrap.views.column,name="column"),
    path('bootstrap/flex_desine',bootstrap.views.flex_desine,name="flex_desine"),
    path('bootstrap/bootstrap_custom',bootstrap.views.bootstrap_custom,name="bootstrap_custom"),

]
