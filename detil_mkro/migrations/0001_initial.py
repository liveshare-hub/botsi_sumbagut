# Generated by Django 3.2.6 on 2021-08-07 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DetilMkro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npp', models.CharField(max_length=12)),
                ('div_1', models.CharField(max_length=3)),
                ('nama_prsh', models.CharField(max_length=100)),
                ('keps_awal', models.CharField(max_length=8)),
                ('keps_jp', models.CharField(blank=True, max_length=8, null=True)),
                ('blth_na', models.CharField(blank=True, max_length=8, null=True)),
                ('pareto', models.CharField(blank=True, max_length=10, null=True)),
                ('skl_usaha', models.CharField(choices=[('M', 'Mikro'), ('K', 'Kecil'), ('MN', 'Menengah'), ('B', 'Besar')], default='M', max_length=2)),
                ('prog', models.CharField(choices=[('2P', '(JKK, JKM)'), ('3P', '(JKK, JKM, JHT)'), ('4P', '(JKK, JKM, JHT, JP)')], default='2P', max_length=2)),
                ('tambah_tk', models.IntegerField(default=0)),
                ('kurang_tk', models.IntegerField(default=0)),
                ('total_tk_aktif', models.IntegerField(default=0)),
                ('total_tk_na', models.IntegerField(default=0)),
                ('jml_all_tk', models.IntegerField(default=0)),
                ('total_iuran_berjalan', models.BigIntegerField(default=0)),
                ('blth_siap_rekon', models.CharField(max_length=8)),
                ('btlh_akir', models.CharField(max_length=8)),
                ('nilai_posting', models.BigIntegerField(default=0)),
                ('sipp', models.IntegerField(choices=[(0, 'T'), (1, 'Y')], default=0)),
                ('itw', models.IntegerField(choices=[(0, 'T'), (1, 'Y')], default=0)),
                ('ibr_ijt', models.BigIntegerField(default=0)),
                ('ibr_idm', models.BigIntegerField(default=0)),
                ('ix', models.IntegerField(choices=[(0, 'T'), (1, 'Y')], default=0)),
                ('tgl_upload', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]