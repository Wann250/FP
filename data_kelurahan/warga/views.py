from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Warga, Pengaduan
from django.urls import reverse_lazy
from .forms import WargaForm, PengaduanForm
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import WargaSerializer, PengaduanSerializer
# Create your views here.

class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html' 
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')


class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'                       

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

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html' 
    success_url = reverse_lazy('pengaduan-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')

class WargaListAPIView(ListAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class WargaDetailAPIView(RetrieveAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class PengaduanListAPIView(ListAPIView):
    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer

class PengaduanDetailAPIView(RetrieveAPIView):
    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer
