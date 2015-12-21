from django.contrib import admin
from web.models import *

# Register your models here

class BaseAdmin(admin.ModelAdmin):
    #list_display = ('ad','display_photo',)
    #fields = ('sira', 'image','aciklama', )
    #readonly_fields = ('sira', 'image', 'aciklama', )

    def display_photo(self,obj):
        if obj.id and obj.foto:
            return '<img src="%s" height="80px;">' % obj.foto.url
        return ''
    display_photo.allow_tags = True


class SliderAdmin(BaseAdmin):
    list_display = ('aciklama', 'sira', 'display_photo', )


class EfsaneAdmin(BaseAdmin):
    list_display = ('ad','sira','display_photo',)


class SponsorAdmin(BaseAdmin):
    list_display = ('ad','display_photo',)


class TakimAdmin(BaseAdmin):
    list_display = ('takim_adi','display_photo',)


class SezonTakimAdmin(admin.ModelAdmin):
    list_display = ('takim','sezon',)


class BaskanAdmin(BaseAdmin):
    list_display = ('ad','sira', 'display_photo', )

class TeknikHeyetAdmin(BaseAdmin):
    list_display = ('ad', 'gorev', 'sira', 'display_photo',)

class YonetimAdmin(BaseAdmin):
    list_display = ('ad', 'gorev', 'sira', 'display_photo',)

class FutbolcuAdmin(BaseAdmin):
    list_display = ('ad', 'mevki', 'sira', 'display_photo',)

class SonuclarAdmin(admin.ModelAdmin):
    list_display = ('sezon', 'hafta', 'ev_sahibi', 'ev_sahibi_skor', 'misafir', 'misafir_skor',)

class GaleriAdmin(BaseAdmin):
    list_display = ('display_photo',)

class HaberAdmin(admin.ModelAdmin):
    list_display = ('baslik','olusturulma_tarihi',)

class OnurKuruluAdmin(BaseAdmin):
    list_display = ('ad', 'sira', 'display_photo',)



admin.site.register(Haber, HaberAdmin)
admin.site.register(SiteAyarlar)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Efsaneler, EfsaneAdmin)
admin.site.register(Sponsorlar, SponsorAdmin)
admin.site.register(Takimlar, TakimAdmin)
admin.site.register(Sezon)
admin.site.register(Sezon_takimlar, SezonTakimAdmin)
admin.site.register(Baskanlar, BaskanAdmin)
admin.site.register(TeknikHeyet, TeknikHeyetAdmin)
admin.site.register(Yonetim, YonetimAdmin)
admin.site.register(Sonuclar, SonuclarAdmin)
admin.site.register(Futbolcular, FutbolcuAdmin)
admin.site.register(StadFotolari, GaleriAdmin)
admin.site.register(TesisFotolari, GaleriAdmin)
admin.site.register(NostaljiFotolari, GaleriAdmin)
admin.site.register(OnurKurulu,OnurKuruluAdmin)