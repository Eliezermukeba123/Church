from django import forms
from django.contrib.auth.models import User

from .models import Menbres, Quartier, Fonction, Diacre, Administateur, Comite, Evenement


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
             'class': 'bg-gray-50 py-2 border w-full border border-gray-300 rounded-xl text-gray-500 h-12 px-1 outline-none mb-4',
            'placeholder': "Entrez votre nom d'utilisateur",
        }),
        label="Nom"

    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'bg-gray-50 py-2 border w-full border border-gray-300 rounded-xl h-12 text-gray-500 px-1 outline-none mb-4',
            'placeholder': "Entrez votre mot de passe",
        }),
        label="Mot de passe"
    )

    class Meta:
        model = User
        fields = ("username", "password")


class MenbresForm(forms.ModelForm):
    class Meta:
        model = Menbres
        fields = ['nom', 'postnom', 'prenom', 'date', 'genre', 'Adresse', 'email', 'telephone', 'statut', 'etat_civil', 'photo', 'quartier', 'groupe_sanguin', 'fonction']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'genre': forms.RadioSelect(choices=Menbres.GENRE_CHOICES),
            'statut': forms.RadioSelect(choices=Menbres.STATUT_CHOICES),
            'etat_civil': forms.RadioSelect(choices=Menbres.Etat_CHOICES),
            'groupe_sanguin': forms.RadioSelect(choices=Menbres.SANG_CHOICES),
        }
        labels = {
            'adresse': 'Adresse',
            'etat_civil': 'État civil',
            'groupe_sanguin': 'Groupe sanguin',
        }


class QuartierForm(forms.ModelForm):
    class Meta:
        model = Quartier
        fields = ['nom', 'delimitation']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'delimitation': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'nom': 'Nom du quartier',
            'delimitation': 'Limitations du quartier',
        }


class FonctionForm(forms.ModelForm):
    class Meta:
        model = Fonction
        fields = ['nom',]
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nom': 'Nom',
        }


class DiacreForm(forms.ModelForm):
    fonction = Fonction.objects.get(nom="Diacre")
    id_menbre = forms.ModelChoiceField(queryset=Menbres.objects.filter(fonction=fonction), label="Membre")

    class Meta:
        model = Diacre
        fields = ['id_menbre', 'profession', 'debut_mandat', 'fin_mandat', 'etat_mandat']
        widgets = {
            'debut_mandat': forms.DateInput(attrs={'type': 'date'}),
            'fin_mandat': forms.DateInput(attrs={'type': 'date'}),
            'etat_mandat': forms.RadioSelect(choices=Diacre.ETAT_MANDAT_CHOICES),
        }
        labels = {
            'id_menbre': 'Membre',
            'debut_mandat': 'Début mandat',
            'fin_mandat': 'Fin mandat',
            'etat_mandat': 'État du mandat',
        }


class AdministateurForm(forms.ModelForm):
    administateur = Fonction.objects.get(nom="Administrateur")
    id_menbre = forms.ModelChoiceField(queryset=Menbres.objects.filter(fonction=administateur), label="Membre")

    class Meta:
        model = Administateur
        fields = ['id_menbre', 'profession', 'debut_mandat', 'fin_mandat', 'etat_mandat']
        widgets = {
            'debut_mandat': forms.DateInput(attrs={'type': 'date'}),
            'fin_mandat': forms.DateInput(attrs={'type': 'date'}),
            'etat_mandat': forms.RadioSelect(choices=Administateur.ETAT_MANDAT_CHOICES),
        }
        labels = {
            'id_menbre': 'Membre',
            'debut_mandat': 'Début mandat',
            'fin_mandat': 'Fin mandat',
            'etat_mandat': 'État du mandat',
        }


class ComiteForm(forms.ModelForm):
    quartier = forms.ModelChoiceField(queryset=Quartier.objects.all(), label="Quartier")
    menbre = forms.ModelChoiceField(queryset=Menbres.objects.all(), label="Membre")
    class Meta:
        model = Comite
        fields = ['quartier', 'menbre', 'fonction']
        widgets = {
            'fonction': forms.RadioSelect(choices=Comite.Fonction_CHOICES),
        }
        labels = {
            'menbre': 'Membre',

        }


class EvenementForm(forms.ModelForm):
    class Meta:
        model = Evenement
        fields = ['type_even', 'date_even', 'heure_even', 'place_even', 'membres']
        widgets = {
            'date_even': forms.DateInput(attrs={'type': 'date'}),
            'heure_even': forms.TimeInput(attrs={'type': 'time'}),
            'membres': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['membres'].required = False
