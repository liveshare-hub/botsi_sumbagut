# Generated by Django 3.2.6 on 2021-08-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_extenduser_token_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='extenduser',
            name='tgl_token',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
