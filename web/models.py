from django.db import models
from django.contrib.auth.models import User


class Haber(models.Model):
    baslik = models.CharField(max_length=255)
    icerik = models.TextField()
    olusturulma_tarihi =models.DateTimeField(auto_now_add=True, auto_now=False)
    kullanici = models.ForeignKey(User)
    foto = models.ImageField(upload_to='media',blank=True)

    def __str__(self):
        return self.baslik

    class Meta:
        verbose_name = 'Haber'
        verbose_name_plural = 'Haberler'
