# notas/views.py
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import Notas

def notas(request):

    notas = Notas.objects.all()

    return render(request, 'notas.html', {'notas': notas})

def agregar_nota(request):

    notas = Notas.objects.all()

    return render(request, 'agregar_nota.html', {'notas': notas})
