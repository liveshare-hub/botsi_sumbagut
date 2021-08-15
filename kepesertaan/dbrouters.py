from .models import TargetRealisasi, JenisUraian, Uraian
from accounts.models import m_jabatan, m_bidang, kode_kantor, ExtendUser
from detil_mkro.models import DetilMkro
from django.conf import settings

class KepesertaanDBRouter:
    def db_for_read(self, model, **hints):
        if (model == DetilMkro):
            return 'primary'
        elif (model == TargetRealisasi) or (model == JenisUraian) or (model == Uraian):
            return 'default'
        return None
    
    def db_for_write(self, model, **hints):
        if (model == TargetRealisasi) or (model == JenisUraian) or (model == Uraian):
            return 'default'

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in settings.DATABASES:
            return db == 'default'
        return None