from django.db import models

class DetilMkro(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    prov = models.CharField(db_column='PROV', max_length=20)  # Field name made lowercase.
    kluster = models.CharField(db_column='KLUSTER', max_length=5)  # Field name made lowercase.
    kode_kantor = models.CharField(db_column='KODE_KANTOR', max_length=3)  # Field name made lowercase.
    nama_kantor = models.CharField(db_column='NAMA_KANTOR', max_length=50)  # Field name made lowercase.
    kode_pembina = models.CharField(db_column='KODE_PEMBINA', max_length=8)  # Field name made lowercase.
    nama_pembina = models.CharField(db_column='NAMA_PEMBINA', max_length=100)  # Field name made lowercase.
    npp = models.CharField(db_column='NPP', max_length=12)  # Field name made lowercase.
    div_1 = models.CharField(db_column='DIV_1', max_length=3)  # Field name made lowercase.
    nama_prsh = models.CharField(db_column='NAMA_PRSH', max_length=100)  # Field name made lowercase.
    keps_awal = models.CharField(db_column='KEPS_AWAL', max_length=8)  # Field name made lowercase.
    keps_jp = models.CharField(db_column='KEPS_JP', max_length=8)  # Field name made lowercase.
    blth_na = models.CharField(db_column='BLTH_NA', max_length=8)  # Field name made lowercase.
    pareto = models.CharField(db_column='PARETO', max_length=10)  # Field name made lowercase.
    skl_usaha = models.CharField(db_column='SKL_USAHA', max_length=20)  # Field name made lowercase.
    prog = models.CharField(db_column='PROG', max_length=2)  # Field name made lowercase.
    tambah_tk = models.IntegerField(db_column='TAMBAH_TK')  # Field name made lowercase.
    kurang_tk = models.IntegerField(db_column='KURANG_TK')  # Field name made lowercase.
    total_tk_aktif = models.IntegerField(db_column='TOTAL_TK_AKTIF')  # Field name made lowercase.
    total_tk_na = models.IntegerField(db_column='TOTAL_TK_NA')  # Field name made lowercase.
    jml_all_tk = models.IntegerField(db_column='JML_ALL_TK')  # Field name made lowercase.
    total_iuran_berjalan = models.BigIntegerField(db_column='TOTAL_IURAN_BERJALAN')  # Field name made lowercase.
    blth_siap_rekon = models.CharField(db_column='BLTH_SIAP_REKON', max_length=8)  # Field name made lowercase.
    blth_akhir = models.CharField(db_column='BLTH_AKHIR', max_length=8)  # Field name made lowercase.
    nilai_posting = models.BigIntegerField(db_column='NILAI_POSTING')  # Field name made lowercase.
    sipp = models.IntegerField(db_column='SIPP')  # Field name made lowercase.
    itw = models.IntegerField(db_column='ITW')  # Field name made lowercase.
    ibr_ijt = models.BigIntegerField(db_column='IBR_IJT')  # Field name made lowercase.
    ibr_idm = models.BigIntegerField(db_column='IBR_IDM')  # Field name made lowercase.
    ix = models.IntegerField(db_column='IX')  # Field name made lowercase.
    tgl_upload = models.DateTimeField(db_column='TGL_UPLOAD')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'detil_mkro'

    def __str__(self):
        return '{} - {}'.format(self.npp, self.nama_prsh)