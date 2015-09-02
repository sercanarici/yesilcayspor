from django.shortcuts import render
from web.models import Haber


def index(request):
    haberler = Haber.objects.all()[:5]
    return render(request,"index.html",locals())


def fikstur(request):
    return render(request,"fikstur.html",locals())


def haber_detay(request, haber_id):
    haber = Haber.objects.get(pk=haber_id)
    return render(request,"haber_detay.html",locals())


def stadimiz(request):
    return render(request,"stadimiz.html",locals())


def tarihce(request):
    return render(request,"tarihce.html",locals())


def tesislerimiz(request):
    return render(request,"tesislerimiz.html",locals())


def deneme(request):
    x = Haber.objects.all()
    return render(request,"test.html",locals())

