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
    foto = models.ImageField(upload_to='slider')
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

class Takimlar(models.Model):
    takim_adi = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='takimlar', default='takimlar/nologo.png')

    class Meta:
        verbose_name = 'takım'
        verbose_name_plural = 'takımlar'

    def __str__(self):
        return self.takim_adi


class Sezon(models.Model):
    adi = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Sezon'
        verbose_name_plural ='Sezonlar'

    def __str__(self):
        return  self.adi

class Sezon_takimlar(models.Model):
    sezon = models.ForeignKey(Sezon)
    takim = models.ForeignKey(Takimlar)

    class Meta:
        verbose_name = 'Sezon Takım'
        verbose_name_plural ='Sezonun Takımları'
        unique_together = ('sezon','takim',)

    def __str__(self):
        return self.takim.takim_adi


class Baskanlar(models.Model):
    ad = models.CharField(max_length=100)
    gorev_yili = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='baskanlar', default='baskanlar/default.png')
    sira = models.IntegerField(verbose_name='sıra', blank=True, default=0)

    class Meta:
        verbose_name = "Başkan"
        verbose_name_plural = 'Başkanlar'

    def __str__(self):
        return self.ad

