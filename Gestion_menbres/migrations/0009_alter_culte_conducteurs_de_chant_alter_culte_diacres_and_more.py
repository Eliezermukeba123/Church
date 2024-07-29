# Generated by Django 4.2.7 on 2024-07-25 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_menbres', '0008_culte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culte',
            name='conducteurs_de_chant',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='culte',
            name='diacres',
            field=models.ManyToManyField(blank=True, related_name='Diacres', to='Gestion_menbres.menbres'),
        ),
        migrations.AlterField(
            model_name='culte',
            name='heure_fin',
            field=models.TimeField(blank=True, verbose_name='Fin service'),
        ),
        migrations.AlterField(
            model_name='culte',
            name='nombre_construction',
            field=models.PositiveIntegerField(blank=True, verbose_name='Offrande de Construction'),
        ),
        migrations.AlterField(
            model_name='culte',
            name='nombre_dimes',
            field=models.PositiveIntegerField(blank=True, verbose_name='Dïmes'),
        ),
        migrations.AlterField(
            model_name='culte',
            name='nombre_membres',
            field=models.PositiveIntegerField(blank=True, verbose_name='Effectif Total'),
        ),
        migrations.AlterField(
            model_name='culte',
            name='nombre_offrandes',
            field=models.PositiveIntegerField(blank=True, verbose_name='Offrande Régulier'),
        ),
    ]
