# notas/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('notas/', views.notas, name='notas'),
    path('agregar-nota/', views.agregar_nota, name='agregar_nota'),
]