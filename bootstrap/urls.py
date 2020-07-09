from django.urls import path
from . import views

urlpatterns = [
    path('',views.bootstrap,name="bootstrap"),
    path('ui/',views.ui,name="ui"),
    path('use_ui/',views.use_ui,name="use_ui"),
    path('make_navbar/',views.make_navbar,name="make_navbar"),
    path('breakpoint/',views.breakpoint,name="breakpoint"),
    path('dark_light/',views.dark_light,name="dark_light"),
    path('grid/',views.grid,name="grid"),
    path('row_col/',views.row_col,name="row_col"),
    path('column/',views.column,name="column"),
    path('flex_desine/',views.flex_desine,name="flex_desine"),
    path('bootstrap_custom/',views.bootstrap_custom,name="bootstrap_custom"),
      
]
