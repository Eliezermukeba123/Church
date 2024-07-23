import django_filters
from django.forms import DateInput
from django.utils import timezone
from django_filters import CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    nom = CharFilter(method='filter_nom',label='')
    class Meta:
        model = Menbres
        fields = ('quartier', 'statut', 'etat_civil', 'groupe_sanguin','nom')

    def filter_nom(self, queryset, name, value):
        if value:
            queryset = queryset.filter(
                models.Q(nom__icontains=value) |
                models.Q(postnom__icontains=value) |
                models.Q(prenom__icontains=value)
            )
        return queryset


class QuartierFilter(django_filters.FilterSet):
    nom = CharFilter(method='filter_nom',label='Nom')
    delimitation = CharFilter(method='del_nom',label='Emplacement')
    class Meta:
        model = Quartier
        fields = ('nom', 'delimitation')

    def filter_nom(self, queryset, name, value):
        if value:
            queryset = queryset.filter(
                models.Q(nom__icontains=value)
            )
        return queryset

    def del_nom(self, queryset, name, value):
        if value:
            queryset = queryset.filter(
                models.Q(delimitation__icontains=value)
            )
        return queryset


class FonctionFilter(django_filters.FilterSet):
    nom = CharFilter(method='filter_nom',label='Nom')
    class Meta:
        model = Fonction
        fields = ('nom',)

    def filter_nom(self, queryset, name, value):
        if value:
            queryset = queryset.filter(
                models.Q(nom__icontains=value)
            )
        return queryset


class DiacreFilter(django_filters.FilterSet):
    id_menbre__nom = django_filters.CharFilter(field_name='id_menbre__nom', lookup_expr='icontains', label='Nom du membre')
    profession = django_filters.CharFilter(lookup_expr='icontains', label='Profession')
    etat_mandat = django_filters.ChoiceFilter(choices=Diacre.ETAT_MANDAT_CHOICES, label='État du mandat')
    debut_mandat__gte = django_filters.DateFilter(
        field_name='debut_mandat',
        lookup_expr='gte',
        label='Début de mandat à partir de',
        widget=DateInput(attrs={'type': 'date'})
    )
    fin_mandat__lte = django_filters.DateFilter(
        field_name='fin_mandat',
        lookup_expr='lte',
        label='Fin de mandat jusqu\'à',
        widget=DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = Diacre
        fields = ['id_menbre__nom', 'profession', 'etat_mandat', 'debut_mandat__gte', 'fin_mandat__lte']


class AdministateurFilter(django_filters.FilterSet):
    id_menbre__nom = django_filters.CharFilter(field_name='id_menbre__nom', lookup_expr='icontains', label='Nom du membre')
    profession = django_filters.CharFilter(lookup_expr='icontains', label='Profession')
    etat_mandat = django_filters.ChoiceFilter(choices=Diacre.ETAT_MANDAT_CHOICES, label='État du mandat')
    debut_mandat__gte = django_filters.DateFilter(
        field_name='debut_mandat',
        lookup_expr='gte',
        label='Début de mandat à partir de',
        widget=DateInput(attrs={'type': 'date'})
    )
    fin_mandat__lte = django_filters.DateFilter(
        field_name='fin_mandat',
        lookup_expr='lte',
        label='Fin de mandat jusqu\'à',
        widget=DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = Administateur
        fields = ['id_menbre__nom', 'profession', 'etat_mandat', 'debut_mandat__gte', 'fin_mandat__lte']


class EvenementFilter(django_filters.FilterSet):
    date_even = django_filters.DateFilter(
        field_name='date_even',
        lookup_expr='exact',
        widget=DateInput(attrs={'type': 'date'})
    )
    type_even = django_filters.CharFilter(field_name='type_even', lookup_expr='icontains')
    date_even_month = django_filters.NumberFilter(
        field_name='date_even',
        lookup_expr='month',
        label='Mois précis',
        initial=timezone.now().month
    )

    class Meta:
        model = Evenement
        fields = ['date_even', 'type_even']