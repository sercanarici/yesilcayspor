from django.shortcuts import render, render_to_response
from web.models import Haber, SiteAyarlar, Slider, Efsaneler, Sponsorlar, Baskanlar, TeknikHeyet, Yonetim, Futbolcular, Sonuclar, StadFotolari, TesisFotolari, NostaljiFotolari
from web.puan_durumu import PuanDurum
from django.shortcuts import RequestContext



def bad_request(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def index(request):
    haberler = Haber.objects.all()[:5]
    slides = Slider.objects.all().order_by('sira')
    efsaneler = Efsaneler.objects.all().order_by('sira')
    sponsorlar = Sponsorlar.objects.all()
    return render(request, "index.html", locals())


def fikstur(request):
    ayar = SiteAyarlar.objects.all()
    frame = ''
    try:
        frame = ayar[0].fikstur_link
    except IndexError:
        print("Site ayarlarında fikstür linkini giriniz.")

    return render(request, "fikstur.html", locals())


def haberler(request):
    haberler = Haber.objects.all().order_by('olusturulma_tarihi')
    return render(request, "haberler.html", locals())


def haber_detay(request, haber_id):
    haber = Haber.objects.get(pk=haber_id)
    return render(request, "haber_detay.html", locals())


def stadimiz(request):
    fotolar = StadFotolari.objects.all()
    return render(request, "stadimiz.html", locals())


def tarihce(request):
    ayar = SiteAyarlar.objects.all()
    icerik = ''
    try:
        icerik = ayar[0].tarihce
    except IndexError:
        print("Site ayarlarında icerik alanını doldurunuz.")

    return render(request, "tarihce.html", locals())


def tesislerimiz(request):
    fotolar = TesisFotolari.objects.all()
    return render(request, "tesislerimiz.html", locals())


def baskanlar(request):
    baskanlar = Baskanlar.objects.all().order_by('sira')
    return render(request, "baskanlar.html", locals())


def teknikheyet(request):
    teknikheyet = TeknikHeyet.objects.all().order_by('sira')
    return render(request, "teknik-heyet.html", locals())


def efsaneler(request):
    efsaneler = Efsaneler.objects.all().order_by('sira')
    return render(request, "efsaneler.html", locals())


def yonetim(request):
    yonetim = Yonetim.objects.all().order_by('sira')
    return render(request, "yonetim.html", locals())


def futbolcular(request):
    futbolcular = Futbolcular.objects.all().order_by('sira')
    return render(request, "futbolcular.html", locals())


def iletisim(request):
    ayar = SiteAyarlar.objects.all()
    icerik = ''
    try:
        icerik = ayar[0].iletisim
    except IndexError:
        icerik ="Site ayarlarında iletisim alanını doldurunuz."

    return render(request, "iletisim.html", locals())


def nostalji_fotolar(request):
    fotolar = NostaljiFotolari.objects.all()
    return render(request, "nostalji-galeri.html", locals())


def basvuru(request):
    return render(request, "404.html", locals())



