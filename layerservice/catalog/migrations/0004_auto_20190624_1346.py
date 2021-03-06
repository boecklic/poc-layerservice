# Generated by Django 2.2 on 2019-06-24 13:46

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0002_auto_20190509_1405'),
        ('translation', '0002_auto_20190509_1223'),
        ('catalog', '0003_auto_20190624_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cataloglayer',
            name='bodm_legacy_catalog_id',
        ),
        migrations.RemoveField(
            model_name='cataloglayer',
            name='level',
        ),
        migrations.RemoveField(
            model_name='cataloglayer',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='cataloglayer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cataloglayer',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='cataloglayer',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='cataloglayer',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='cataloglayer',
            name='tree_id',
        ),
        migrations.CreateModel(
            name='CatalogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bodm_legacy_catalog_id', models.IntegerField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('datasets', models.ManyToManyField(through='catalog.CatalogLayer', to='layers.Dataset')),
                ('name', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='catalog_cataloglayer_name', to='translation.TranslationKey', verbose_name='name')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalog.CatalogEntry')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Topic')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='cataloglayer',
            name='catalog_entry',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='catalog.CatalogEntry'),
            preserve_default=False,
        ),
    ]
