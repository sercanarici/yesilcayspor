from django.shortcuts import render, render_to_response
from web.models import Haber, SiteAyarlar, Slider, Efsaneler, Sponsorlar, Baskanlar
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
    except AttributeError:
        print("Site ayarlarında fikstür linkini giriniz.")

    return render(request, "fikstur.html", locals())


def haberler(request):
    haberler = Haber.objects.all()
    return render(request, "haberler.html", locals())


def haber_detay(request, haber_id):
    haber = Haber.objects.get(pk=haber_id)
    return render(request, "haber_detay.html", locals())


def stadimiz(request):
    return render(request, "stadimiz.html", locals())


def tarihce(request):
    ayar = SiteAyarlar.objects.all()
    icerik = ayar[0].tarihce
    return render(request, "tarihce.html", locals())


def tesislerimiz(request):
    return render(request, "tesislerimiz.html", locals())


def baskanlar(request):
    baskanlar = Baskanlar.objects.all().order_by('sira')
    return render(request, "baskanlar.html", locals())


def efsaneler(request):
    return render(request, "404.html", locals())


def yonetim(request):
    return render(request, "404.html", locals())


def basvuru(request):
    return render(request, "404.html", locals())


def teknikheyet(request):
    return render(request, "404.html", locals())


def futbolcular(request):
    return render(request, "404.html", locals())

def futbolcular(request):
    return render(request, "404.html", locals())

def nostalji(request):
    return render(request, "404.html", locals())

def iletisim(request):
    return render(request, "404.html", locals())

