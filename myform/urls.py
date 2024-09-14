from django.urls import path

from . import views 

app_name= 'myform'

urlpatterns = [
    path('form/',views.form_view, name='form'),
]


