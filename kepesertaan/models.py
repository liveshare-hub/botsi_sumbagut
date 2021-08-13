from django.db import models

from accounts.models import ExtendUser


class JenisUraian(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Uraian(models.Model):
    # jenis = models.ForeignKey(JenisUraian, on_delete=models.CASCADE)
    nama_uraian = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nama_uraian)


class TargetRealisasi(models.Model):
    user = models.ForeignKey(ExtendUser, on_delete=models.CASCADE)
    jenis = models.ForeignKey(JenisUraian, on_delete=models.CASCADE)
    uraian = models.ForeignKey(Uraian, on_delete=models.CASCADE)
    target_tahun = models.CharField(max_length=50, null=True, blank=True)
    target_bln_lapor = models.CharField(max_length=50, null=True, blank=True)
    realisasi_sd_bln_lalu = models.CharField(max_length=50, null=True, blank=True)
    realisasi_bln_lapor = models.CharField(max_length=50, null=True, blank=True)
    realisasi_sd_bln_lapor = models.CharField(max_length=50, null=True, blank=True)
    periode = models.DateField()
    tgl_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uraian.nama_uraian