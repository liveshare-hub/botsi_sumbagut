from django.urls import path

from . import views

app_name = 'entry'
urlpatterns = [
    path('entry_list/', views.entry_list, name='entry_list'),
    path('entry_tambah/', views.entry_tambah, name='entry_tambah'),

]
