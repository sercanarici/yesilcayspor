# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import ckeditor_uploader.fields
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baskanlar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ad', models.CharField(max_length=100)),
                ('gorev_yili', models.CharField(max_length=20)),
                ('sira', models.IntegerField(blank=True, default=0, verbose_name='sıra')),
                ('foto', filer.fields.image.FilerImageField(related_name='baskan_foto', null=True, blank=True, to='filer.Image')),
            ],
            options={
                'verbose_name_plural': 'Başkanlar',
                'verbose_name': 'Başkan',
            },
        ),
        migrations.CreateModel(
            name='Efsaneler',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ad', models.CharField(max_length=100)),
                ('mevki', models.CharField(blank=True, max_length=20)),
                ('sira', models.IntegerField(blank=True, verbose_name='sıra')),
                ('foto', filer.fields.image.FilerImageField(related_name='efsane_foto', null=True, blank=True, to='filer.Image')),
            ],
            options={
                'verbose_name_plural': 'Efsaneler',
                'verbose_name': 'Efsane',
            },
        ),
        migrations.CreateModel(
            name='Haber',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('baslik', models.CharField(max_length=255)),
                ('icerik', ckeditor_uploader.fields.RichTextUploadingField()),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('foto', filer.fields.image.FilerImageField(related_name='haber_foto', null=True, blank=True, to='filer.Image')),
                ('kullanici', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Haberler',
                'verbose_name': 'Haber',
            },
        ),
        migrations.CreateModel(
            name='Sezon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('adi', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Sezonlar',
                'verbose_name': 'Sezon',
            },
        ),
        migrations.CreateModel(
            name='Sezon_takimlar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('sezon', models.ForeignKey(to='web.Sezon')),
            ],
            options={
                'verbose_name_plural': 'Sezonun Takımları',
                'verbose_name': 'Sezon Takım',
            },
        ),
        migrations.CreateModel(
            name='SiteAyarlar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('fikstur_link', models.URLField(blank=True)),
                ('tarihce', ckeditor.fields.RichTextField()),
                ('site', models.OneToOneField(to='sites.Site')),
            ],
            options={
                'verbose_name_plural': 'Site Ayarları',
                'verbose_name': 'Site Ayarları',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('aciklama', models.CharField(max_length=200)),
                ('sira', models.IntegerField(verbose_name='sıra')),
                ('foto', filer.fields.image.FilerImageField(related_name='slider_foto', null=True, blank=True, help_text='Düzgün görünebilmesi için 1184x400 boyutlarında olması gerekir.', to='filer.Image')),
            ],
            options={
                'verbose_name_plural': 'Slider',
                'verbose_name': 'Slider',
            },
        ),
        migrations.CreateModel(
            name='Sponsorlar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ad', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=255, default='#')),
                ('foto', filer.fields.image.FilerImageField(related_name='sponsor_foto', null=True, blank=True, to='filer.Image')),
            ],
            options={
                'verbose_name_plural': 'Sponsorlar',
                'verbose_name': 'Sponsor',
            },
        ),
        migrations.CreateModel(
            name='Takimlar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('takim_adi', models.CharField(max_length=100)),
                ('foto', filer.fields.image.FilerImageField(related_name='takim_foto', null=True, blank=True, to='filer.Image')),
            ],
            options={
                'verbose_name_plural': 'takımlar',
                'verbose_name': 'takım',
            },
        ),
        migrations.CreateModel(
            name='TeknikHeyet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ad', models.CharField(max_length=50)),
                ('sira', models.IntegerField(blank=True, default=0, verbose_name='sıra')),
                ('gorev', models.CharField(max_length=50)),
                ('foto', filer.fields.image.FilerImageField(related_name='gorevli_foto', null=True, blank=True, to='filer.Image')),
            ],
            options={
                'verbose_name_plural': 'Teknik Heyet',
                'verbose_name': 'Görevli',
            },
        ),
        migrations.CreateModel(
            name='Yonetim',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ad', models.CharField(max_length=50)),
                ('sira', models.IntegerField(blank=True, default=0, verbose_name='sıra')),
                ('gorev', models.CharField(max_length=50)),
                ('foto', filer.fields.image.FilerImageField(related_name='yonetici_foto', null=True, blank=True, to='filer.Image')),
            ],
            options={
                'verbose_name_plural': 'Yönetim',
                'verbose_name': 'Yönetici',
            },
        ),
        migrations.AddField(
            model_name='sezon_takimlar',
            name='takim',
            field=models.ForeignKey(to='web.Takimlar'),
        ),
        migrations.AlterUniqueTogether(
            name='sezon_takimlar',
            unique_together=set([('sezon', 'takim')]),
        ),
    ]
