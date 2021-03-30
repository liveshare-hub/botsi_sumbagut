from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class BuatRencana(models.Model):
    judul = models.CharField(max_length=100)
    isi = models.TextField()
    tgl_eksekusi = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('tgl_eksekusi',)
        verbose_name = 'Rencana'
        verbose_name_plural = 'Daftar Rencana'

    def __str__(self):
        return str(self.judul)
