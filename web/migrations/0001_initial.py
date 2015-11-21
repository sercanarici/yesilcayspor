# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Efsaneler',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('ad', models.CharField(max_length=100)),
                ('fornma_no', models.CharField(max_length=3, blank=True)),
                ('mevki', models.CharField(max_length=20, blank=True)),
                ('sira', models.IntegerField(verbose_name='sıra')),
            ],
            options={
                'verbose_name': 'Efsane',
                'verbose_name_plural': 'Efsaneler',
            },
        ),
        migrations.CreateModel(
            name='Haber',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('baslik', models.CharField(max_length=255)),
                ('icerik', ckeditor_uploader.fields.RichTextUploadingField()),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('foto', models.ImageField(upload_to='media', blank=True)),
                ('kullanici', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Haber',
                'verbose_name_plural': 'Haberler',
            },
        ),
        migrations.CreateModel(
            name='SiteAyarlar',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('fikstur_link', models.URLField(blank=True)),
                ('tarihce', ckeditor.fields.RichTextField()),
                ('site', models.OneToOneField(to='sites.Site')),
            ],
            options={
                'verbose_name': 'Site Ayarları',
                'verbose_name_plural': 'Site Ayarları',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('aciklama', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='slider')),
                ('sira', models.IntegerField(verbose_name='sıra')),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Slider',
            },
        ),
    ]
