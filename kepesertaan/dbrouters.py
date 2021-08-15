from .models import TargetRealisasi, JenisUraian, Uraian
from accounts.models import m_jabatan, m_bidang, kode_kantor, ExtendUser
from detil_mkro.models import DetilMkro

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

    def allow_migrate(self, model, **hints):
        if (model == TargetRealisasi) or (model == JenisUraian) or (model == Uraian)\
            or (model == m_bidang) or (model == m_jabatan) or (model == kode_kantor)\
                or (model == ExtendUser)
            return 'default'
        return None