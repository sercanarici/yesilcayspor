# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('twitter', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('photo', models.URLField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'User Detail',
                'verbose_name': 'User Detail',
            },
        ),
    ]
