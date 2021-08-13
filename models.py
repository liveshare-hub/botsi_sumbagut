# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DetilBsu(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    kode_segmen = models.CharField(db_column='KODE_SEGMEN', max_length=10)  # Field name made lowercase.
    kode_wilayah = models.CharField(db_column='KODE_WILAYAH', max_length=10)  # Field name made lowercase.
    kode_kantor = models.CharField(db_column='KODE_KANTOR', max_length=10)  # Field name made lowercase.
    kode_kepesertaan = models.CharField(db_column='KODE_KEPESERTAAN', max_length=10)  # Field name made lowercase.
    kode_perusahaan = models.CharField(db_column='KODE_PERUSAHAAN', max_length=10)  # Field name made lowercase.
    npp = models.CharField(db_column='NPP', max_length=12)  # Field name made lowercase.
    nama_perusahaan = models.CharField(db_column='NAMA_PERUSAHAAN', max_length=100)  # Field name made lowercase.
    alamat_perusahaan = models.TextField(db_column='ALAMAT_PERUSAHAAN')  # Field name made lowercase.
    kode_provinsi = models.CharField(db_column='KODE_PROVINSI', max_length=10)  # Field name made lowercase.
    nama_provinsi = models.CharField(db_column='NAMA_PROVINSI', max_length=100)  # Field name made lowercase.
    kode_kabupaten = models.CharField(db_column='KODE_KABUPATEN', max_length=10)  # Field name made lowercase.
    nama_kabupaten = models.CharField(db_column='NAMA_KABUPATEN', max_length=100)  # Field name made lowercase.
    kode_ilo = models.CharField(db_column='KODE_ILO', max_length=10)  # Field name made lowercase.
    nama_ilo = models.CharField(db_column='NAMA_ILO', max_length=100)  # Field name made lowercase.
    nama_lapangan_usaha = models.CharField(db_column='NAMA_LAPANGAN_USAHA', max_length=100)  # Field name made lowercase.
    nama_pic_prs = models.CharField(db_column='NAMA_PIC_PRS', max_length=100)  # Field name made lowercase.
    hp_pic_prs = models.CharField(db_column='HP_PIC_PRS', max_length=50)  # Field name made lowercase.
    kode_usaha_utama = models.CharField(db_column='KODE_USAHA_UTAMA', max_length=10)  # Field name made lowercase.
    kode_kepemilikan = models.CharField(db_column='KODE_KEPEMILIKAN', max_length=10)  # Field name made lowercase.
    kode_tk = models.CharField(db_column='KODE_TK', max_length=20)  # Field name made lowercase.
    kpj = models.CharField(db_column='KPJ', max_length=20)  # Field name made lowercase.
    nomor_identitas = models.CharField(db_column='NOMOR_IDENTITAS', max_length=20)  # Field name made lowercase.
    status_valid_identitas = models.CharField(db_column='STATUS_VALID_IDENTITAS', max_length=10)  # Field name made lowercase.
    jenis_identitas = models.CharField(db_column='JENIS_IDENTITAS', max_length=20)  # Field name made lowercase.
    tgl_kepesertaan = models.CharField(db_column='TGL_KEPESERTAAN', max_length=100)  # Field name made lowercase.
    nama_lengkap = models.CharField(db_column='NAMA_LENGKAP', max_length=100)  # Field name made lowercase.
    tgl_lahir = models.CharField(db_column='TGL_LAHIR', max_length=100)  # Field name made lowercase.
    tpt_lahir = models.CharField(db_column='TPT_LAHIR', max_length=100)  # Field name made lowercase.
    jenis_kelamin = models.CharField(db_column='JENIS_KELAMIN', max_length=10)  # Field name made lowercase.
    nama_ibu_kandung = models.CharField(db_column='NAMA_IBU_KANDUNG', max_length=100)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=100)  # Field name made lowercase.
    handphone = models.CharField(db_column='HANDPHONE', max_length=20)  # Field name made lowercase.
    hp_kominfo = models.CharField(db_column='HP_KOMINFO', max_length=20)  # Field name made lowercase.
    no_rekening = models.CharField(db_column='NO_REKENING', max_length=100)  # Field name made lowercase.
    kode_bank = models.CharField(db_column='KODE_BANK', max_length=10)  # Field name made lowercase.
    nama_bank = models.CharField(db_column='NAMA_BANK', max_length=100)  # Field name made lowercase.
    status_verivali = models.CharField(db_column='STATUS_VERIVALI', max_length=10)  # Field name made lowercase.
    tgl_update = models.DateTimeField(db_column='TGL_UPDATE')  # Field name made lowercase.
    tgl_upload = models.DateTimeField(db_column='TGL_UPLOAD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detil_bsu'


class DetilGeotag(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    prov = models.CharField(db_column='PROV', max_length=20)  # Field name made lowercase.
    kluster = models.CharField(db_column='KLUSTER', max_length=5)  # Field name made lowercase.
    kode_kantor = models.CharField(db_column='KODE_KANTOR', max_length=5)  # Field name made lowercase.
    nama_kantor = models.CharField(db_column='NAMA_KANTOR', max_length=50)  # Field name made lowercase.
    nama_pembina = models.CharField(db_column='NAMA_PEMBINA', max_length=60)  # Field name made lowercase.
    npp = models.CharField(db_column='NPP', max_length=20)  # Field name made lowercase.
    divi = models.CharField(db_column='DIVI', max_length=5)  # Field name made lowercase.
    kode_sub = models.IntegerField(db_column='KODE_SUB')  # Field name made lowercase.
    nama_prsh = models.CharField(db_column='NAMA_PRSH', max_length=60)  # Field name made lowercase.
    blth_keps = models.CharField(db_column='BLTH_KEPS', max_length=15)  # Field name made lowercase.
    blth_na = models.CharField(db_column='BLTH_NA', max_length=15)  # Field name made lowercase.
    skl_ush = models.CharField(db_column='SKL_USH', max_length=5)  # Field name made lowercase.
    alamat = models.CharField(db_column='ALAMAT', max_length=300)  # Field name made lowercase.
    lat = models.FloatField(db_column='LAT')  # Field name made lowercase.
    lon = models.FloatField(db_column='LON')  # Field name made lowercase.
    kode_tlp = models.IntegerField(db_column='KODE_TLP')  # Field name made lowercase.
    nomor1 = models.IntegerField(db_column='NOMOR1')  # Field name made lowercase.
    nomor2 = models.IntegerField(db_column='NOMOR2')  # Field name made lowercase.
    fax = models.IntegerField(db_column='FAX')  # Field name made lowercase.
    tgl_input = models.DateTimeField(db_column='TGL_INPUT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detil_geotag'


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
        managed = False
        db_table = 'detil_mkro'


class DetilPembayaran(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    npp = models.CharField(db_column='NPP', max_length=20)  # Field name made lowercase.
    divi = models.CharField(db_column='DIVI', max_length=3)  # Field name made lowercase.
    nama_prsh = models.CharField(db_column='NAMA_PRSH', max_length=100)  # Field name made lowercase.
    blth_keps = models.CharField(db_column='BLTH_KEPS', max_length=7)  # Field name made lowercase.
    blth_jp = models.CharField(db_column='BLTH_JP', max_length=7)  # Field name made lowercase.
    blth_awal = models.CharField(db_column='BLTH_AWAL', max_length=7)  # Field name made lowercase.
    blth_akhir = models.CharField(db_column='BLTH_AKHIR', max_length=7)  # Field name made lowercase.
    kanal = models.CharField(db_column='KANAL', max_length=8)  # Field name made lowercase.
    no_trx = models.CharField(db_column='NO_TRX', max_length=40)  # Field name made lowercase.
    tgl_bayar = models.CharField(db_column='TGL_BAYAR', max_length=10)  # Field name made lowercase.
    tgl_trx = models.CharField(db_column='TGL_TRX', max_length=10)  # Field name made lowercase.
    nilai = models.BigIntegerField(db_column='NILAI')  # Field name made lowercase.
    jht = models.BigIntegerField(db_column='JHT')  # Field name made lowercase.
    jkk = models.BigIntegerField(db_column='JKK')  # Field name made lowercase.
    jkm = models.BigIntegerField(db_column='JKM')  # Field name made lowercase.
    jp = models.BigIntegerField(db_column='JP')  # Field name made lowercase.
    denda = models.BigIntegerField(db_column='DENDA')  # Field name made lowercase.
    total_posting = models.BigIntegerField(db_column='TOTAL_POSTING')  # Field name made lowercase.
    tgl_input = models.DateTimeField(db_column='TGL_INPUT')  # Field name made lowercase.
    nama_pembina = models.CharField(db_column='NAMA_PEMBINA', max_length=100)  # Field name made lowercase.
    kode_kantor = models.CharField(db_column='KODE_KANTOR', max_length=100)  # Field name made lowercase.
    nama_kantor = models.CharField(db_column='NAMA_KANTOR', max_length=50)  # Field name made lowercase.
    kode_pembina = models.CharField(db_column='KODE_PEMBINA', max_length=12)  # Field name made lowercase.
    kluster = models.CharField(db_column='KLUSTER', max_length=5)  # Field name made lowercase.
    prov = models.CharField(db_column='PROV', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detil_pembayaran'


class DetilValidPkbu(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    prov = models.CharField(db_column='PROV', max_length=20)  # Field name made lowercase.
    kluster = models.CharField(db_column='KLUSTER', max_length=5)  # Field name made lowercase.
    kode_kantor = models.CharField(db_column='KODE_KANTOR', max_length=3)  # Field name made lowercase.
    nama_kantor = models.CharField(db_column='NAMA_KANTOR', max_length=50)  # Field name made lowercase.
    kode_pembina = models.CharField(db_column='KODE_PEMBINA', max_length=8)  # Field name made lowercase.
    nama_pembina = models.CharField(db_column='NAMA_PEMBINA', max_length=100)  # Field name made lowercase.
    npp = models.CharField(db_column='NPP', max_length=12)  # Field name made lowercase.
    skala = models.CharField(db_column='SKALA', max_length=50)  # Field name made lowercase.
    div_1 = models.CharField(db_column='DIV_1', max_length=3)  # Field name made lowercase.
    nama_prsh = models.CharField(db_column='NAMA_PRSH', max_length=100)  # Field name made lowercase.
    alamat = models.CharField(db_column='ALAMAT', max_length=1)  # Field name made lowercase.
    kode_pos = models.CharField(db_column='KODE_POS', max_length=1)  # Field name made lowercase.
    npwp = models.CharField(db_column='NPWP', max_length=1)  # Field name made lowercase.
    no_telp = models.CharField(db_column='NO_TELP', max_length=1)  # Field name made lowercase.
    email_kantor = models.CharField(db_column='EMAIL_KANTOR', max_length=1)  # Field name made lowercase.
    nama_pic = models.CharField(db_column='NAMA_PIC', max_length=1)  # Field name made lowercase.
    jabatan_pic = models.CharField(db_column='JABATAN_PIC', max_length=1)  # Field name made lowercase.
    no_pic = models.CharField(db_column='NO_PIC', max_length=1)  # Field name made lowercase.
    email_pic = models.CharField(db_column='EMAIL_PIC', max_length=1)  # Field name made lowercase.
    nama_pemilik = models.CharField(db_column='NAMA_PEMILIK', max_length=1)  # Field name made lowercase.
    validitas = models.CharField(db_column='VALIDITAS', max_length=1)  # Field name made lowercase.
    tgl_input = models.DateTimeField(db_column='TGL_INPUT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detil_valid_pkbu'


class GeotagData(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    prov = models.CharField(db_column='PROV', max_length=20)  # Field name made lowercase.
    kluster = models.CharField(db_column='KLUSTER', max_length=5)  # Field name made lowercase.
    kode_kantor = models.CharField(db_column='KODE_KANTOR', max_length=3)  # Field name made lowercase.
    nama_kantor = models.TextField(db_column='NAMA_KANTOR')  # Field name made lowercase.
    nama_pembina = models.TextField(db_column='NAMA_PEMBINA')  # Field name made lowercase.
    geotag_aktif = models.CharField(db_column='GEOTAG_AKTIF', max_length=10)  # Field name made lowercase.
    geotag_nonaktif = models.CharField(db_column='GEOTAG_NONAKTIF', max_length=10)  # Field name made lowercase.
    pkbu_aktif = models.IntegerField(db_column='PKBU_AKTIF')  # Field name made lowercase.
    belum_tag = models.IntegerField(db_column='BELUM_TAG')  # Field name made lowercase.
    persen_prog = models.FloatField(db_column='PERSEN_PROG')  # Field name made lowercase.
    tgl_input = models.DateTimeField(db_column='TGL_INPUT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geotag_data'


class LagaGeotag(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    prov = models.CharField(db_column='PROV', max_length=20)  # Field name made lowercase.
    kluster = models.CharField(db_column='KLUSTER', max_length=5)  # Field name made lowercase.
    kode_kantor = models.CharField(db_column='KODE_KANTOR', max_length=5)  # Field name made lowercase.
    nama_kantor = models.CharField(db_column='NAMA_KANTOR', max_length=50)  # Field name made lowercase.
    kode_pembina = models.CharField(db_column='KODE_PEMBINA', max_length=8)  # Field name made lowercase.
    nama_pembina = models.CharField(db_column='NAMA_PEMBINA', max_length=60)  # Field name made lowercase.
    npp = models.CharField(db_column='NPP', max_length=20)  # Field name made lowercase.
    divi = models.IntegerField(db_column='DIVI')  # Field name made lowercase.
    nama_prsh = models.CharField(db_column='NAMA_PRSH', max_length=60)  # Field name made lowercase.
    skl_usaha = models.CharField(db_column='SKL_USAHA', max_length=5)  # Field name made lowercase.
    status_y = models.IntegerField(db_column='STATUS_Y')  # Field name made lowercase.
    status_t = models.IntegerField(db_column='STATUS_T')  # Field name made lowercase.
    tgl_input = models.DateTimeField(db_column='TGL_INPUT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'laga_geotag'


class RekapMkro(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    kode_kantor = models.CharField(db_column='KODE_KANTOR', max_length=3)  # Field name made lowercase.
    kode_pembina = models.CharField(db_column='KODE_PEMBINA', max_length=80)  # Field name made lowercase.
    nama_pembina = models.CharField(db_column='NAMA_PEMBINA', max_length=50)  # Field name made lowercase.
    bu_aktif = models.IntegerField(db_column='BU_AKTIF')  # Field name made lowercase.
    bu_na = models.IntegerField(db_column='BU_NA')  # Field name made lowercase.
    number_2p = models.IntegerField(db_column='2P')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3p = models.IntegerField(db_column='3P')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_4p = models.IntegerField(db_column='4P')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    skl_besar = models.IntegerField(db_column='SKL_BESAR')  # Field name made lowercase.
    skl_mngh = models.IntegerField(db_column='SKL_MNGH')  # Field name made lowercase.
    skl_kecil = models.IntegerField(db_column='SKL_KECIL')  # Field name made lowercase.
    skl_mikro = models.IntegerField(db_column='SKL_MIKRO')  # Field name made lowercase.
    tk_tambah = models.IntegerField(db_column='TK_TAMBAH')  # Field name made lowercase.
    tk_kurang = models.IntegerField(db_column='TK_KURANG')  # Field name made lowercase.
    tk_aktif = models.IntegerField(db_column='TK_AKTIF')  # Field name made lowercase.
    tk_na = models.IntegerField(db_column='TK_NA')  # Field name made lowercase.
    tk_total = models.IntegerField(db_column='TK_TOTAL')  # Field name made lowercase.
    total_iuran = models.BigIntegerField(db_column='TOTAL_IURAN')  # Field name made lowercase.
    nilai_posting = models.BigIntegerField(db_column='NILAI_POSTING')  # Field name made lowercase.
    mobile = models.IntegerField(db_column='MOBILE')  # Field name made lowercase.
    esaldo = models.IntegerField(db_column='ESALDO')  # Field name made lowercase.
    sms = models.IntegerField(db_column='SMS')  # Field name made lowercase.
    sipp = models.IntegerField(db_column='SIPP')  # Field name made lowercase.
    rmdr = models.IntegerField(db_column='RMDR')  # Field name made lowercase.
    rkn_oto = models.IntegerField(db_column='RKN_OTO')  # Field name made lowercase.
    apld_dok = models.IntegerField(db_column='APLD_DOK')  # Field name made lowercase.
    itw = models.IntegerField(db_column='ITW')  # Field name made lowercase.
    itb = models.IntegerField(db_column='ITB')  # Field name made lowercase.
    nik_valid = models.IntegerField(db_column='NIK_VALID')  # Field name made lowercase.
    nik_invalid = models.IntegerField(db_column='NIK_INVALID')  # Field name made lowercase.
    ijt = models.BigIntegerField(db_column='IJT')  # Field name made lowercase.
    idm = models.BigIntegerField(db_column='IDM')  # Field name made lowercase.
    tgl_upld = models.DateTimeField(db_column='TGL_UPLD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rekap_mkro'


class TblAkuisisiTk(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    prov = models.CharField(db_column='PROV', max_length=20)  # Field name made lowercase.
    kluster = models.CharField(db_column='KLUSTER', max_length=5)  # Field name made lowercase.
    kode_kantor = models.CharField(db_column='KODE_KANTOR', max_length=3)  # Field name made lowercase.
    nama_kantor = models.CharField(db_column='NAMA_KANTOR', max_length=50)  # Field name made lowercase.
    kode_pembina = models.CharField(db_column='KODE_PEMBINA', max_length=8)  # Field name made lowercase.
    nama_pembina = models.CharField(db_column='NAMA_PEMBINA', max_length=60)  # Field name made lowercase.
    tk_baru = models.IntegerField(db_column='TK_BARU')  # Field name made lowercase.
    nik_valid = models.IntegerField(db_column='NIK_VALID')  # Field name made lowercase.
    nik_invalid = models.IntegerField(db_column='NIK_INVALID')  # Field name made lowercase.
    tgl_upload = models.DateTimeField(db_column='TGL_UPLOAD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_akuisisi_tk'


class TblDetilNik(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    prov = models.CharField(db_column='PROV', max_length=20)  # Field name made lowercase.
    kluster = models.CharField(db_column='KLUSTER', max_length=5)  # Field name made lowercase.
    kode_kantor = models.CharField(db_column='KODE_KANTOR', max_length=3)  # Field name made lowercase.
    nama_kantor = models.CharField(db_column='NAMA_KANTOR', max_length=50)  # Field name made lowercase.
    kode_pembina = models.CharField(db_column='KODE_PEMBINA', max_length=8)  # Field name made lowercase.
    nama_pembina = models.CharField(db_column='NAMA_PEMBINA', max_length=60)  # Field name made lowercase.
    npp = models.CharField(db_column='NPP', max_length=20)  # Field name made lowercase.
    divi = models.CharField(db_column='DIVI', max_length=5)  # Field name made lowercase.
    nama_prsh = models.CharField(db_column='NAMA_PRSH', max_length=100)  # Field name made lowercase.
    kpj = models.CharField(db_column='KPJ', max_length=40)  # Field name made lowercase.
    nama_tk = models.CharField(db_column='NAMA_TK', max_length=100)  # Field name made lowercase.
    nik = models.CharField(db_column='NIK', max_length=40)  # Field name made lowercase.
    tgl_lahir = models.CharField(db_column='TGL_LAHIR', max_length=40)  # Field name made lowercase.
    tempat_lahir = models.CharField(db_column='TEMPAT_LAHIR', max_length=100)  # Field name made lowercase.
    jenis_kelamin = models.CharField(db_column='JENIS_KELAMIN', max_length=20)  # Field name made lowercase.
    nama_ibu = models.CharField(db_column='NAMA_IBU', max_length=100)  # Field name made lowercase.
    status_kepsertaan = models.CharField(db_column='STATUS_KEPSERTAAN', max_length=1)  # Field name made lowercase.
    status_valid = models.CharField(db_column='STATUS_VALID', max_length=1)  # Field name made lowercase.
    tgl_update = models.DateTimeField(db_column='TGL_UPDATE')  # Field name made lowercase.
    tgl_input = models.DateTimeField(db_column='TGL_INPUT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_detil_nik'


class TblItwitb(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    prov = models.CharField(db_column='PROV', max_length=20)  # Field name made lowercase.
    kluster = models.CharField(db_column='KLUSTER', max_length=5)  # Field name made lowercase.
    kode_kantor = models.CharField(db_column='KODE_KANTOR', max_length=3)  # Field name made lowercase.
    nama_kantor = models.CharField(db_column='NAMA_KANTOR', max_length=60)  # Field name made lowercase.
    nama_pembina = models.CharField(db_column='NAMA_PEMBINA', max_length=80)  # Field name made lowercase.
    pkbu_aktif = models.IntegerField(db_column='PKBU_AKTIF')  # Field name made lowercase.
    pkbu_itw = models.IntegerField(db_column='PKBU_ITW')  # Field name made lowercase.
    persen_itw = models.FloatField(db_column='PERSEN_ITW')  # Field name made lowercase.
    target_itb = models.IntegerField(db_column='TARGET_ITB')  # Field name made lowercase.
    pkbu_itb = models.IntegerField(db_column='PKBU_ITB')  # Field name made lowercase.
    persen_itb = models.FloatField(db_column='PERSEN_ITB')  # Field name made lowercase.
    tgl_upload = models.DateTimeField(db_column='TGL_UPLOAD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_itwitb'


class TblKantor(models.Model):
    kode_kantor = models.CharField(db_column='KODE_KANTOR', primary_key=True, max_length=3)  # Field name made lowercase.
    kode_cabang = models.CharField(db_column='KODE_CABANG', max_length=3)  # Field name made lowercase.
    kode_kanwil = models.CharField(db_column='KODE_KANWIL', max_length=3)  # Field name made lowercase.
    nama_kantor = models.CharField(db_column='NAMA_KANTOR', max_length=100)  # Field name made lowercase.
    kluster = models.CharField(db_column='KLUSTER', max_length=20)  # Field name made lowercase.
    prov = models.CharField(db_column='PROV', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_kantor'


class TblKepsAktif(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    prov = models.CharField(db_column='PROV', max_length=20)  # Field name made lowercase.
    kluster = models.CharField(db_column='KLUSTER', max_length=5)  # Field name made lowercase.
    kode_kantor = models.CharField(db_column='KODE_KANTOR', max_length=3)  # Field name made lowercase.
    nama_kantor = models.CharField(db_column='NAMA_KANTOR', max_length=50)  # Field name made lowercase.
    kode_pembina = models.CharField(db_column='KODE_PEMBINA', max_length=8)  # Field name made lowercase.
    nama_pembina = models.CharField(db_column='NAMA_PEMBINA', max_length=60)  # Field name made lowercase.
    pkbu_aktif = models.IntegerField(db_column='PKBU_AKTIF')  # Field name made lowercase.
    tk_aktif = models.IntegerField(db_column='TK_AKTIF')  # Field name made lowercase.
    pkbu_na = models.IntegerField(db_column='PKBU_NA')  # Field name made lowercase.
    tk_na = models.IntegerField(db_column='TK_NA')  # Field name made lowercase.
    tgl_upload = models.DateTimeField(db_column='TGL_UPLOAD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_keps_aktif'


class TblRekapNik(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    prov = models.CharField(db_column='PROV', max_length=20)  # Field name made lowercase.
    kluster = models.CharField(db_column='KLUSTER', max_length=5)  # Field name made lowercase.
    kode_kantor = models.CharField(db_column='KODE_KANTOR', max_length=3)  # Field name made lowercase.
    nama_kantor = models.CharField(db_column='NAMA_KANTOR', max_length=50)  # Field name made lowercase.
    kode_pembina = models.CharField(db_column='KODE_PEMBINA', max_length=8)  # Field name made lowercase.
    nama_pembina = models.CharField(db_column='NAMA_PEMBINA', max_length=60)  # Field name made lowercase.
    total_binaan = models.IntegerField(db_column='TOTAL_BINAAN')  # Field name made lowercase.
    npwp_valid = models.IntegerField(db_column='NPWP_VALID')  # Field name made lowercase.
    npwp_invalid = models.IntegerField(db_column='NPWP_INVALID')  # Field name made lowercase.
    persen_npwp_valid = models.FloatField(db_column='PERSEN_NPWP_VALID')  # Field name made lowercase.
    total_tk_aktif = models.IntegerField(db_column='TOTAL_TK_AKTIF')  # Field name made lowercase.
    nik_valid_aktif = models.IntegerField(db_column='NIK_VALID_AKTIF')  # Field name made lowercase.
    persen_nik_valid_aktif = models.FloatField(db_column='PERSEN_NIK_VALID_AKTIF')  # Field name made lowercase.
    nik_invalid_aktif = models.IntegerField(db_column='NIK_INVALID_AKTIF')  # Field name made lowercase.
    persen_nik_invalid_aktif = models.FloatField(db_column='PERSEN_NIK_INVALID_AKTIF')  # Field name made lowercase.
    total_tk_na = models.IntegerField(db_column='TOTAL_TK_NA')  # Field name made lowercase.
    nik_valid_na = models.IntegerField(db_column='NIK_VALID_NA')  # Field name made lowercase.
    persen_nik_valid_na = models.FloatField(db_column='PERSEN_NIK_VALID_NA')  # Field name made lowercase.
    nik_invalid_na = models.IntegerField(db_column='NIK_INVALID_NA')  # Field name made lowercase.
    persen_nik_invalid_na = models.FloatField(db_column='PERSEN_NIK_INVALID_NA')  # Field name made lowercase.
    tgl_input = models.DateTimeField(db_column='TGL_INPUT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_rekap_nik'


class TblTargetKepesertaan(models.Model):
    perusahaan = models.IntegerField()
    tk_pu = models.IntegerField()
    tk_bpu = models.IntegerField()
    tk_jakon = models.IntegerField()
    iuran_pu = models.BigIntegerField()
    iuran_bpu = models.BigIntegerField()
    iuran_jakon = models.BigIntegerField()
    bu_aktif = models.IntegerField()
    pu_aktif = models.IntegerField()
    bpu_aktif = models.IntegerField()
    jakon_aktif = models.IntegerField()
    tanggal = models.DateTimeField()
    tahun = models.TextField()  # This field type is a guess.
    user_id = models.CharField(max_length=8)
    kode_kantor = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'tbl_target_kepesertaan'
