# Generated by Django 4.2.7 on 2024-07-29 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_menbres', '0015_remove_culte_nombre_dimes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culte',
            name='nombre_construction',
            field=models.FloatField(blank=True, default=0.0, verbose_name='Offrande de Construction'),
        ),
        migrations.AlterField(
            model_name='culte',
            name='nombre_offrandes',
            field=models.FloatField(blank=True, default=0.0, verbose_name='Offrande Régulier'),
        ),
    ]
