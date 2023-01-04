from django.urls import path
from app1.views import *
app_name='something2'

urlpatterns=[
    path('reddy/',reddy,name='reddy'),
]