# Generated by Django 1.11.14 on 2019-03-06 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0004_auto_20190306_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervention',
            name='stake',
            field=models.ForeignKey(blank=True, db_column='enjeu', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interventions', to='core.Stake', verbose_name='Stake'),
        ),
    ]
