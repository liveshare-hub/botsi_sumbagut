from django import forms
from datetime import date, timedelta
from accounts.models import kode_kantor



class TargetForm(forms.Form):
    kd_kantor = forms.ModelChoiceField(queryset=kode_kantor.objects.all(),
        widget=forms.Select(attrs={
            'class':'form-control','id':'kd_kantor'
        }), initial=kode_kantor.objects.filter(kd_kantor='A00'))

    tgl = forms.DateField(initial=date.today(), widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date', 'id': 'tgl'}))

    class Meta:
        fields = ['kd_kantor','tgl']