from django.urls import path
from .views import index, verifikasi

urlpatterns = [
    path('cari', index),
    path('activate/<str:token>', verifikasi),
]
