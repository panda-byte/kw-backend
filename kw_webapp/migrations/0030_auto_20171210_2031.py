# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-11 01:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kw_webapp', '0029_auto_20171125_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answersynonym',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reading_synonyms', to='kw_webapp.UserSpecific'),
        ),
        migrations.AlterField(
            model_name='meaningsynonym',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meaning_synonyms', to='kw_webapp.UserSpecific'),
        ),
    ]
