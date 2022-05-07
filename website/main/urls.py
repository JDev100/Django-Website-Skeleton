from venv import create
from django.urls import path

from . import views

urlpatterns = [
    #pick view based on path
    path("<int:id>", views.index, name="list"),
    path("", views.home, name = "home"),    
    path("create/", views.create, name = "create")    
]