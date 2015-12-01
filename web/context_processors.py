from web.models import Sonuclar
from web.puan_durumu import PuanDurum


def mac_sonuclar(requst):
    return {'mac_sonuclar' : Sonuclar.objects.all().order_by('-hafta')}


def puan_durum(request):
    return {'puan_durum': PuanDurum.puan_durumu()}