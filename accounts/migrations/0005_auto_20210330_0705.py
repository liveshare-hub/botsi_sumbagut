# Generated by Django 3.1.7 on 2021-03-30 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210330_0704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bidang',
            name='created',
        ),
        migrations.RemoveField(
            model_name='bidang',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='role',
            name='created',
        ),
        migrations.RemoveField(
            model_name='role',
            name='updated',
        ),
    ]
