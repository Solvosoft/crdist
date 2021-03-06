# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 05:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crdist', '0002_load_intial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crdist.District')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prov', to='crdist.District')),
            ],
        ),
    ]
