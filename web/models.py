from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site


class Haber(models.Model):
    baslik = models.CharField(max_length=255)
    icerik = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True, auto_now=False)
    kullanici = models.ForeignKey(User)
    foto = models.ImageField(upload_to='media',blank=True)

    def __str__(self):
        return self.baslik

    class Meta:
        verbose_name = 'Haber'
        verbose_name_plural = 'Haberler'


class Tarihce(models.Model):
    baslik = models.CharField(max_length=100)
    icerik = models.TextField()

    def __str__(self):
        return self.baslik

    class Meta:
        verbose_name = 'Tarihçe'
        verbose_name_plural = 'Tarihçe'


class SiteAyarlar(models.Model):
    site = models.OneToOneField(Site)
    fikstur_link = models.URLField(blank=True)
    tarihce = models.TextField(blank=True)

    class Meta:
        verbose_name = "Site Ayarları"
        verbose_name_plural = "Site Ayarları"

    def __str__(self):
        return self.site.name
