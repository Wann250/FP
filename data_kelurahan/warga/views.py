from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Warga, Pengaduan
from django.urls import reverse_lazy
from .forms import WargaForm, PengaduanForm
# Create your views here.

class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga
    context_object_name = 'warga'

class PengaduanListView(ListView):
    model = Pengaduan
    context_object_name = 'pengaduan_list'                       

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')