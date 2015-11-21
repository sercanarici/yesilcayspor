from django.contrib import admin
from web.models import *

# Register your models here


class SliderAdmin(admin.ModelAdmin):
    list_display = ('aciklama', 'sira', 'display_photo', )
    #fields = ('sira', 'image','aciklama', )
    #readonly_fields = ('sira', 'image', 'aciklama', )

    def display_photo(self, obj):
        if obj.id:
            return '<img src="%s" height="100">' % obj.image.url
        return ''
    display_photo.allow_tags = True


class EfsaneAdmin(admin.ModelAdmin):
    list_display = ('ad','sira','display_photo',)

    def display_photo(self,obj):
        if obj.id:
            return '<img src="%s" height="100">' % obj.foto.url
        return ''
    display_photo.allow_tags = True


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('ad','display_photo',)

    def display_photo(self,obj):
        if obj.id:
            return '<img src="%s" height="100">' % obj.foto.url
        return ''
    display_photo.allow_tags = True



admin.site.register(Haber)
admin.site.register(SiteAyarlar)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Efsaneler, EfsaneAdmin)
admin.site.register(Sponsorlar,SponsorAdmin)

