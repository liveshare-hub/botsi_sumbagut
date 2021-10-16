from django.urls import path
from .views import index

urlpatterns = [
    path('cari', index),
    # path('activate/<str:token>', verifikasi),
]
