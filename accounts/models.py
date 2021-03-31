from django.db import models
from django.contrib.auth.models import User


class Bidang(models.Model):
    nama = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nama',)
        verbose_name = 'Bidang'
        verbose_name_plural = 'Daftar Bidang'

    def __str__(self):
        return self.nama


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200)
    bidang = models.ForeignKey(Bidang, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nama',)
        verbose_name = 'Profile User'
        verbose_name_plural = 'Daftar Profile User'

    def __str__(self):
        return self.nama
