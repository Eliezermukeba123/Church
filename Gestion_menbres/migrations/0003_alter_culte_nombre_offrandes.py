# Generated by Django 4.2.7 on 2024-08-06 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_menbres', '0002_joursemaine_evenement_autres_evenement_heure_even_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culte',
            name='nombre_offrandes',
            field=models.FloatField(blank=True, default=0.0, verbose_name='Offrande Régulière'),
        ),
    ]
