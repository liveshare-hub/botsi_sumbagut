from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import BuatRencana
from accounts.models import Bidang, UserAccount
from .forms import BuatRencanaForm


# Entry
@login_required(login_url="/login/")
def entry_list(request):
    is_staff = request.user.is_staff
    is_kabid = request.user.is_kabid
    bidang = request.user.bidang
    if is_staff:
        entry_list = BuatRencana.objects.all()
    else:
        if is_kabid:
            entry_list = BuatRencana.objects.filter(user__bidang=bidang)
        else:
            entry_list = BuatRencana.objects.filter(user=request.user)

    context = {
        'entry_list': entry_list,
    }
    return render(request, "entry/entry_list.html", context)


@login_required(login_url="/login/")
def entry_tambah(request):
    form = BuatRencanaForm()
    if request.method == 'POST':
        form = BuatRencanaForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('entry:entry_list')

    context = {
        'form_title': 'Entry Tambah',
        'form': form,
    }
    return render(request, 'entry/entry_form.html', context)
