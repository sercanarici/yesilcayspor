from django.contrib import admin
from web.models import *

# Register your models here

class BaseAdmin(admin.ModelAdmin):
    #list_display = ('ad','display_photo',)
    #fields = ('sira', 'image','aciklama', )
    #readonly_fields = ('sira', 'image', 'aciklama', )

    def display_photo(self,obj):
        if obj.id:
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


admin.site.register(Haber)
admin.site.register(SiteAyarlar)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Efsaneler, EfsaneAdmin)
admin.site.register(Sponsorlar, SponsorAdmin)
admin.site.register(Takimlar, TakimAdmin)
admin.site.register(Sezon)
admin.site.register(Sezon_takimlar, SezonTakimAdmin)
admin.site.register(Baskanlar, BaskanAdmin)
