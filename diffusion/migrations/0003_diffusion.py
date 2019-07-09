# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-08 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('production', '0008_production_award'),
        ('diffusion', '0002_production_award'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diffusion_meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(blank=True, choices=[(b'WORLD', b'Mondial'), (b'INTER', b'International'), (b'NATIO', b'National')], help_text=b'Qualifies the first broadcast', max_length=5, null=True)),
                ('on_competition', models.BooleanField(default=False, help_text=b'IN / OFF : On competion or not')),
                ('artwork', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='diffusion', to='production.Artwork')),
            ],
        ),
        migrations.CreateModel(
            name='MetaEvent',
            fields=[
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='meta_event', serialize=False, to='production.Event')),
                ('genres', multiselectfield.db.fields.MultiSelectField(choices=[(b'FILM', b'Films'), (b'PERF', b'Performances'), (b'INST', b'Installations')], help_text=b'Global kind of productions shown', max_length=14)),
                ('important', models.BooleanField(default=True, help_text=b'Helps hide minor events')),
                ('keywords', taggit.managers.TaggableManager(blank=True, help_text=b'Qualifies Festival: digital arts, residency, electronic festival', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.DeleteModel(
            name='Diffusion',
        ),
        migrations.AddField(
            model_name='diffusion_meta',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='production.Event'),
        ),
        migrations.AlterUniqueTogether(
            name='diffusion_meta',
            unique_together=set([('id', 'artwork', 'event')]),
        ),
    ]