# Generated by Django 2.2 on 2019-05-09 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='de',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='translation',
            name='en',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='translation',
            name='fr',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='translation',
            name='it',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='translation',
            name='rm',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='translation',
            name='translation_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translation_versions', to='translation.TranslationKey'),
        ),
    ]
