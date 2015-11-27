"""yesilcayspor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url, patterns, handler404
from django.contrib import admin
from web.views import *

handler404 = 'web.views.bad_request'

urlpatterns = [
    #url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='home'),
    url(r'^fikstur$', fikstur, name='fikstur'),
    url(r'^haberler$', haberler, name='haberler'),
    url(r'^haber_detay/(?P<haber_id>[0-9]+)/$', haber_detay, name='haber_detay'),
    url(r'^stadimiz$', stadimiz, name='stadimiz'),
    url(r'^tarihce$', tarihce, name='tarihce'),
    url(r'^tesislerimiz$', tesislerimiz, name='tesislerimiz'),
    url(r'^baskanlar$', baskanlar, name='baskanlar'),
    url(r'^efsaneler$', efsaneler, name='efsaneler'),
    url(r'^yonetim$', yonetim, name='yonetim'),
    url(r'^basvuru$', basvuru, name='basvuru'),
    url(r'^teknikheyet$', teknikheyet, name='teknikheyet'),
    url(r'^futbolcular$', futbolcular, name='futbolcular'),
    url(r'^nostalji$', nostalji, name='nostalji'),
    url(r'^iletisim$', iletisim, name='iletisim'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^filer/', include('filer.urls')),
]

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )

