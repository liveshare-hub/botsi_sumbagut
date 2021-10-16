from django.shortcuts import render
from django.http import HttpResponse
from .form import TargetForm
from accounts.models import kode_kantor
from .scrapingPDF import Scrapping
from datetime import datetime
# Create your views here.
# from graphql_auth.mixins import UserStatus

def index(request):
    form = TargetForm(request.POST)
    if form.is_valid():
        kantor = request.POST['kd_kantor']
        qs = kode_kantor.objects.get(pk=kantor)
        kd_kantor = qs.kd_kantor
        periode = datetime.strptime(request.POST['tgl'], "%Y-%m-%d").strftime("%d/%m/%Y")
        
        user = request.user

        Scrapping(kd_kantor, periode, user)

        return render(request,'kepesertaan/cari.html',{'form':form})
    else:
        form = TargetForm()

    return render(request,'kepesertaan/cari.html',{'form':form})

# def verifikasi(request, token):
#     UserStatus.verify(token)
#     return HttpResponse({"success":"Akun berhasil di verifikasi"})