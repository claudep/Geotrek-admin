# Generated by Django 1.11.20 on 2019-07-16 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signage', '0007_auto_20190625_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signage',
            name='condition',
            field=models.ForeignKey(blank=True, db_column='etat', null=True, on_delete=django.db.models.deletion.SET_NULL, to='infrastructure.InfrastructureCondition', verbose_name='Condition'),
        ),
    ]
