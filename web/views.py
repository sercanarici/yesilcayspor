from django.shortcuts import render
from web.models import Haber, Tarihce, SiteAyarlar


def index(request):
    haberler = Haber.objects.all()[:5]
    return render(request,"index.html",locals())


def fikstur(request):
    ayar = SiteAyarlar.objects.all()
    frame = ayar[0].fikstur_link
    return render(request, "fikstur.html", locals())


def haberler(request):
    haberler = Haber.objects.all()
    return render(request, "haberler.html", locals())


def haber_detay(request, haber_id):
    haber = Haber.objects.get(pk=haber_id)
    return render(request, "haber_detay.html", locals())


def stadimiz(request):
    return render(request,"stadimiz.html",locals())


def tarihce(request):
    ayar = SiteAyarlar.objects.all()
    icerik = ayar[0].tarihce
    return render(request, "tarihce.html", locals())


def tesislerimiz(request):
    return render(request, "tesislerimiz.html", locals())


def deneme(request):
    x = Haber.objects.all()
    return render(request, "test.html", locals())

