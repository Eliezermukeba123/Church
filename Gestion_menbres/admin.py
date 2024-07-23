from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Pasteur)
class PasteurAdmin(admin.ModelAdmin):
    pass


@admin.register(Diacre)
class DiacreAdmin(admin.ModelAdmin):

    list_filter = ('debut_mandat',)  # Filtres latéraux
    ordering = ('-debut_mandat',)  # Tri par date décroissante
    pass


@admin.register(Administateur)
class AdministateurAdmin(admin.ModelAdmin):
    list_filter = ('debut_mandat',)  # Filtres latéraux
    ordering = ('-debut_mandat',)  # Tri par date décroissante
    pass


@admin.register(Menbres)
class MenbresAdmin(admin.ModelAdmin):
    search_fields = ('nom', 'postnom', 'prenom', 'telephone',)
    list_filter = ('quartier', 'statut', 'etat_civil', 'groupe_sanguin')  # Filtres latéraux
    ordering = ('-date',)  # Tri par date décroissante
    pass


@admin.register(Garde)
class GardeAdmin(admin.ModelAdmin):
    pass


@admin.register(Quartier)
class QuartierAdmin(admin.ModelAdmin):
    search_fields = ('nom','delimitation')
    list_filter = ('nom','delimitation')  # Filtres latéraux
    pass


@admin.register(Gardinage)
class GardinageAdmin(admin.ModelAdmin):
    search_fields = ('date',)
    list_filter = ('date',)  # Filtres latéraux
    ordering = ('-date',)


    pass


@admin.register(Fonction)
class FonctionAdmin(admin.ModelAdmin):
    search_fields = ('nom',)
    list_filter = ('nom',)  # Filtres latéraux
    pass


@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    search_fields = ('type_even',)
    list_filter = ('type_even', 'place_even')  # Filtres latéraux
    ordering = ('-date_even',)
    pass


@admin.register(Communication)
class CommunicationAdmin(admin.ModelAdmin):
    search_fields = ('type_comm', 'date_comm')
    list_filter = ('type_comm', 'date_comm')  # Filtres latéraux
    ordering = ('-date_comm',)
    pass


@admin.register(Activite)
class ActiviteAdmin(admin.ModelAdmin):
    search_fields = ('type_activ',)
    list_filter = ('type_activ', 'place_activ')  # Filtres latéraux
    ordering = ('-date_activ',)
    pass


@admin.register(Offrande)
class OffrandeAdmin(admin.ModelAdmin):
    search_fields = ('type_off',)
    list_filter = ('date_off','type_off')  # Filtres latéraux
    ordering = ('-date_off',)
    pass


@admin.register(Comite)
class ComiteAdmin(admin.ModelAdmin):

    list_filter = ('fonction','quartier')  # Filtres latéraux
    pass


@admin.register(Technique)
class TechniqueAdmin(admin.ModelAdmin):
    list_filter = ('departement',)
    pass


@admin.register(Besoin)
class BesoinAdmin(admin.ModelAdmin):
    pass





