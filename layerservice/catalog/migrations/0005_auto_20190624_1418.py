# Generated by Django 2.2 on 2019-06-24 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20190624_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogentry',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='catalog_cataloglayer_name', to='translation.TranslationKey', verbose_name='name'),
        ),
    ]
