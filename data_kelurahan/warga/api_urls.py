from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WargaViewSet, PengaduanViewSet
# from .views import WargaListAPIView, WargaDetailAPIView, PengaduanListAPIView, PengaduanDetailAPIView


router = DefaultRouter()
router.register('warga', WargaViewSet, basename='warga')
router.register('pengaduan', PengaduanViewSet, basename='pengaduan')

urlpatterns = [
    # path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
    # path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='detail-api-warga-list'),

    # path('pengaduan/', PengaduanListAPIView.as_view(), name='api-pengaduan-list'),
    # path('pengaduan/<int:pk>/', PengaduanDetailAPIView.as_view(),name="detail-api-pengaduan-list"),
    path('', include(router.urls)),
]
