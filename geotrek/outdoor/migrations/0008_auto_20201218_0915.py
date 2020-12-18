# Generated by Django 3.1.4 on 2020-12-18 09:15

from django.db import migrations
import geotrek.outdoor.models


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0007_site_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='orientation',
            field=geotrek.outdoor.models.OrientationField(blank=True, choices=[('N', 'N'), ('S', 'S'), ('E', 'E'), ('W', 'W'), ('NE', 'NE'), ('NW', 'NW'), ('SE', 'SE'), ('SW', 'SW')], max_length=2, verbose_name='Orientation'),
        ),
        migrations.AddField(
            model_name='site',
            name='wind',
            field=geotrek.outdoor.models.OrientationField(blank=True, choices=[('N', 'N'), ('S', 'S'), ('E', 'E'), ('W', 'W'), ('NE', 'NE'), ('NW', 'NW'), ('SE', 'SE'), ('SW', 'SW')], max_length=2, verbose_name='Wind'),
        ),
    ]