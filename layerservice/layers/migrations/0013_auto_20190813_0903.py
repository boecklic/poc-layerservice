# Generated by Django 2.2 on 2019-08-13 09:03

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0002_auto_20190628_0731'),
        ('layers', '0012_auto_20190809_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapServerGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layers.Dataset')),
                ('publication_services', models.ManyToManyField(to='publication.WMS')),
            ],
        ),
        migrations.CreateModel(
            name='MapServerLayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('mapserver_layer_name', models.CharField(blank=True, max_length=512, null=True)),
                ('mapfile', models.TextField()),
                ('mapfile_json', django.contrib.postgres.fields.jsonb.JSONField(blank=True)),
                ('units', models.CharField(choices=[('meters', 'meters')], default='meters', max_length=32)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layers.MapServerGroup')),
            ],
        ),
        migrations.DeleteModel(
            name='MapServerConfig',
        ),
    ]
