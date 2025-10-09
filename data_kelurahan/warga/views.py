from django.shortcuts import render
from django.views.generic import ListView
from .models import Warga

# Create your views here.

class WargaListView(ListView):
    model = Warga