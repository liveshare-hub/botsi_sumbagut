from .models import TargetRealisasi, JenisUraian, Uraian
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
        elif (model == DetilMkro):
            return 'primary'
        return None