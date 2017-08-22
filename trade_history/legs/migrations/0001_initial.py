# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-21 23:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('positions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.CharField(max_length=100)),
                ('spread', models.CharField(max_length=100)),
                ('side', models.CharField(choices=[('BUY', 'BUY'), ('SELL', 'SELL')], max_length=10)),
                ('quantity', models.IntegerField()),
                ('position_effect', models.CharField(choices=[('TO OPEN', 'TO OPEN'), ('TO CLOSE', 'TO CLOSE')], max_length=20)),
                ('expiration', models.CharField(max_length=100)),
                ('strike', models.DecimalField(decimal_places=2, max_digits=10)),
                ('option_type', models.CharField(choices=[('CALL', 'CALL'), ('PUT', 'PUT')], max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='legs', to='positions.Position')),
            ],
        ),
    ]
