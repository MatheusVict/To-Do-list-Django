from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name="about-todo")
]