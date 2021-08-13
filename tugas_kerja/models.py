# from django.db import models
# from accounts.models import ExtendUser

# # Create your models here.
# class TugasKerja(models.Model):
#     user = models.ForeignKey(ExtendUser, on_delete=models.CASCADE)
#     judul = models.CharField(max_length=100, verbose_name="judul")
#     isi = models.TextField(verbose_name="isi")
#     tgl_buat = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.judul