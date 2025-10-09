from django.urls import path
from .views import WargaListView


urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
]


