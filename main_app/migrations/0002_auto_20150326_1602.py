# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zones',
            name='superior_zone',
            field=models.ForeignKey(to='main_app.Zones', null=True),
            preserve_default=True,
        ),
    ]
