from django import forms
from functools import partial

from .models import BuatRencana

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class BuatRencanaForm(forms.ModelForm):
    tgl_eksekusi = forms.DateField(widget=DateInput())

    class Meta:
        model = BuatRencana
        fields = ('judul', 'isi', 'tgl_eksekusi')

        widgets = {
            'judul': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Masukkan masukkan judul',
                       'autofocus': True}),
            'isi': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Masukkan keterangan'}),
        }
