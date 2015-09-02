from django.conf import settings
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
from django.conf.urls import include, url, patterns
from django.contrib import admin
from web.views import index, fikstur, haber_detay, stadimiz, tarihce, tesislerimiz, deneme

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='home'),
    url(r'^fikstur$', fikstur, name='fikstur'),
    url(r'^haber_detay/(?P<haber_id>[0-9]+)/$', haber_detay, name='haber_detay'),
    url(r'^stadimiz$', stadimiz, name='stadimiz'),
    url(r'^tarihce$', tarihce, name='tarihce'),
    url(r'^tesislerimiz$', tesislerimiz, name='tesislerimiz'),
    url(r'^test$', deneme, name='tarihce'),
]

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )

