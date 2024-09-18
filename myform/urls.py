
from django.urls import path

from . import views 

app_name= 'myform'

urlpatterns = [
    path('form/',views.FormView.as_view(), name='form'),
]


