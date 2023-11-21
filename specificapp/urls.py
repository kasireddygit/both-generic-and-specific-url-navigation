from specificapp.views import *
from django.urls import path

app_name='hello'

urlpatterns=[
    path('response1/',response1,name='response1'),
    path('response2/',response2,name='response2'),
]