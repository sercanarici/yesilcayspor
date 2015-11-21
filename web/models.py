from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Haber(models.Model):
    baslik = models.CharField(max_length=255)
    icerik = RichTextUploadingField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True, auto_now=False)
    kullanici = models.ForeignKey(User)
    foto = models.ImageField(upload_to='haber', blank=True)

    def __str__(self):
        return self.baslik

    class Meta:
        verbose_name = 'Haber'
        verbose_name_plural = 'Haberler'


class SiteAyarlar(models.Model):
    site = models.OneToOneField(Site)
    fikstur_link = models.URLField(blank=True)
    tarihce = RichTextField()

    class Meta:
        verbose_name = "Site Ayarları"
        verbose_name_plural = "Site Ayarları"

    def __str__(self):
        return self.site.name


class Slider(models.Model):
    aciklama = models.CharField(max_length=200)
    image = models.ImageField(upload_to='slider')
    sira = models.IntegerField(verbose_name='sıra')

    class Meta:
        verbose_name ="Slider"
        verbose_name_plural="Slider"

    def __str__(self):
        return self.aciklama

class Efsaneler(models.Model):
    ad = models.CharField(max_length=100)
    forma_no = models.CharField(max_length=3, blank=True)
    mevki = models.CharField(max_length=20, blank=True)
    sira = models.IntegerField(verbose_name='sıra', blank=True)
    foto = models.ImageField(upload_to='efsaneler')

    class Meta:
        verbose_name = "Efsane"
        verbose_name_plural = "Efsaneler"

    def __str__(self):
        return self.ad


class Sponsorlar(models.Model):
    ad = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='sponsor')
    url = models.CharField(max_length=255, default='#')

    class Meta:
        verbose_name = "Sponsor"
        verbose_name_plural ="Sponsorlar"

    def __str__(self):
        return self.ad

