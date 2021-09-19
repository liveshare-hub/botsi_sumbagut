from django.db import models
from django.contrib.auth.models import AbstractUser
from kepesertaan.fungsi import generateUniqueCode
import datetime
# Create your models here.

class m_bidang(models.Model):
    nama_bidang = models.CharField(max_length=20)

    def __str__(self):
        return self.nama_bidang

class m_jabatan(models.Model):
    nama_jabatan = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nama_jabatan

class kode_kantor(models.Model):
    provinsi = models.CharField(max_length=50)
    kluster = models.CharField(max_length=3)
    kd_kantor = models.CharField(max_length=5)
    nama_kantor = models.CharField(max_length=50)

    def __str__(self):
        return '{} - {}'.format(self.kd_kantor, self.nama_kantor)


class ExtendUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=100, verbose_name="email")
    jabatan = models.ForeignKey(m_jabatan, on_delete=models.CASCADE, null=True, blank=True,verbose_name="jabatan")
    bidang = models.ForeignKey(m_bidang, on_delete=models.CASCADE, null=True, blank=True,verbose_name="bidang")
    kd_kantor = models.ForeignKey(kode_kantor, on_delete=models.CASCADE,null=True, blank=True, verbose_name="kode kantor")
    id_telegram = models.CharField(blank=True, null=True, max_length=50, verbose_name="telegram")
    token_auth = models.CharField(blank=True, null=True, max_length=200, verbose_name="Token")
    tgl_token = models.DateTimeField(auto_now_add=True)
    updated = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        if self.token_auth == '' or self.token_auth is None:
            self.token_auth = generateUniqueCode()
        if self.jabatan:
            self.updated = True
        super(ExtendUser, self).save(*args, **kwargs)
    

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"


