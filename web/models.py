from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from filer.fields.image import FilerImageField


class Haber(models.Model):
    baslik = models.CharField(max_length=255)
    icerik = RichTextUploadingField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True, auto_now=False)
    kullanici = models.ForeignKey(User)
    foto = FilerImageField(null=True, blank=True, related_name='haber_foto')

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
    foto = FilerImageField(null=True, blank=True, related_name='slider_foto', help_text='Düzgün görünebilmesi için 1184x400 boyutlarında olması gerekir.')
    sira = models.IntegerField(verbose_name='sıra')

    class Meta:
        verbose_name ="Slider"
        verbose_name_plural="Slider"

    def __str__(self):
        return self.aciklama

class Efsaneler(models.Model):
    ad = models.CharField(max_length=100)
    mevki = models.CharField(max_length=20, blank=True)
    sira = models.IntegerField(verbose_name='sıra', blank=True)
    foto = FilerImageField(null=True, blank=True, related_name='efsane_foto')

    class Meta:
        verbose_name = "Efsane"
        verbose_name_plural = "Efsaneler"

    def __str__(self):
        return self.ad


class Sponsorlar(models.Model):
    ad = models.CharField(max_length=50)
    foto = FilerImageField(null=True, blank=True, related_name='sponsor_foto')
    url = models.CharField(max_length=255, default='#')

    class Meta:
        verbose_name = "Sponsor"
        verbose_name_plural ="Sponsorlar"

    def __str__(self):
        return self.ad

class Takimlar(models.Model):
    takim_adi = models.CharField(max_length=100)
    foto = FilerImageField(null=True, blank=True, related_name='takim_foto')
    #foto = models.ImageField(upload_to='takimlar', default='takimlar/nologo.png')

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
    #foto = models.ImageField(upload_to='baskanlar', default='baskanlar/default.png')
    foto = FilerImageField(null=True, blank=True, related_name='baskan_foto')
    sira = models.IntegerField(verbose_name='sıra', blank=True, default=0)

    class Meta:
        verbose_name = "Başkan"
        verbose_name_plural = 'Başkanlar'

    def __str__(self):
        return self.ad

class TeknikHeyet(models.Model):
    ad = models.CharField(max_length=50)
    #foto = models.ImageField(upload_to='teknikheyet', default='teknikheyet/default.png')
    foto = FilerImageField(null=True, blank=True, related_name='gorevli_foto')
    sira = models.IntegerField(verbose_name='sıra', blank=True, default=0)
    gorev = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Görevli'
        verbose_name_plural = "Teknik Heyet"

    def __str__(self):
        return self.ad

class Yonetim(models.Model):
    ad = models.CharField(max_length=50)
    foto = FilerImageField(null=True, blank=True, related_name='yonetici_foto')
    sira = models.IntegerField(verbose_name='sıra', blank=True, default=0)
    gorev = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Yönetici'
        verbose_name_plural = "Yönetim"

    def __str__(self):
        return self.ad


class Futbolcular(models.Model):
    ad = models.CharField(max_length=50)
    foto = FilerImageField(null=True, blank=True, related_name='futbolcu_foto')
    sira = models.IntegerField(verbose_name='sıra', blank=True, default=0)
    mevki = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Futbolcu'
        verbose_name_plural = "Futbolcular"

    def __str__(self):
        return self.ad
