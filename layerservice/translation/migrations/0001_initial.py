# Generated by Django 2.2 on 2019-05-09 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.BooleanField(db_index=True, default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('revision', models.PositiveIntegerField(default=0)),
                ('de', models.CharField(max_length=512, null=True)),
                ('fr', models.CharField(max_length=512, null=True)),
                ('it', models.CharField(max_length=512, null=True)),
                ('en', models.CharField(max_length=512, null=True)),
                ('rm', models.CharField(max_length=512, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TranslationKey',
            fields=[
                ('id', models.SlugField(max_length=512, primary_key=True, serialize=False)),
                ('translation', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_translation_key', to='translation.Translation')),
            ],
        ),
        migrations.AddField(
            model_name='translation',
            name='translation_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translation_version', to='translation.TranslationKey'),
        ),
    ]