from venv import create
from django.urls import path

from . import views

urlpatterns = [
    #pick view based on path
    path("<int:id>", views.index, name="list"),
    path("home/", views.home, name = "home"),    
    path("", views.home, name = "home"),    
    path("view/", views.view, name = "view"),    
    path("create/", views.create, name = "create")    
]