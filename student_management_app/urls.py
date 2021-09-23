from django.conf.urls import url
from django.urls import path

urlpatterns = [
    
]
from django.urls import path
from . import views

urlpatterns=[
    path('demo/',views.demoview)
]