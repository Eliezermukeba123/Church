from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import Page_acceuil, login_view, Pasteur_view, Menbres_view, Detail_membre, logout_view, Diacre_view, \
    Menbres_diacre_view, Detail_membre_diacre, Ajouter_membre_diacre, Modifier_menbre, Quartier_view, \
    Supprimer_Quartier, Modifier_Quartier, Fonction_view, Modifier_Fonction, Supprimer_Fonction, Diacres_view, \
    Ajouter_diacre, Modifier_diacres, Administrateur_view, Ajouter_administrateur, Modifier_administrateur, \
    Comite_quartier, Ajouter_comite, Modifier_comite, Supprimer_Menbre_comite, Evenements, Detail_Evenements

app_name = 'gestMenb'
urlpatterns = [
    # Admin -------------------------------------------------------------------------------------

    path('', login_view, name='login_view'),
    path('logout/', logout_view, name='logout'),
    path('Home', Page_acceuil, name='Page_acceuil'),

    # PASTEUR
    path('Pasteur', Pasteur_view, name='Pasteur_view'),
    path('membres', Menbres_view, name='Menbres_view'),
    path('Detail_membre/<int:cle>/', Detail_membre, name='Detail_membre'),

    # Diacre
    path('Diacre', Diacre_view, name='Diacre_view'),
    path('Diacre/Membres', Menbres_diacre_view, name='Menbres_diacre_view'),
    path('Diacre/Detail_membre/<int:cle>/', Detail_membre_diacre, name='Detail_membre_diacre'),
    path('Diacre/Ajouter', Ajouter_membre_diacre, name='Ajouter_membre_diacre'),
    path('Diacre/Modifier_menbre/<int:cle>/', Modifier_menbre, name='Modifier_menbre'),
    path('Diacre/Quartiers', Quartier_view, name='Quartier_view'),
    path('Diacre/Supprimer_quartier/<int:cle>/', Supprimer_Quartier, name='Supprimer_Quartier'),
    path('Diacre/Modifier_quartier/<int:cle>/', Modifier_Quartier, name='Modifier_Quartier'),
    path('Diacre/Fonctions', Fonction_view, name='Fonction_view'),
    path('Diacre/Modifier_fonction/<int:cle>/', Modifier_Fonction, name='Modifier_Fonction'),
    path('Diacre/Supprimer_fonction/<int:cle>/', Supprimer_Fonction, name='Supprimer_Fonction'),
    path('Diacre/Diagona', Diacres_view, name='Diacres_view'),
    path('Diacre/Insertion', Ajouter_diacre, name='Ajouter_diacre'),
    path('Diacre/Modifier_diacre/<int:cle>/', Modifier_diacres, name='Modifier_diacres'),
    path('Diacre/Administration', Administrateur_view, name='Administrateur_view'),
    path('Diacre/Insertion_Admin', Ajouter_administrateur, name='Ajouter_administrateur'),
    path('Diacre/Modifier_admin/<int:cle>/', Modifier_administrateur, name='Modifier_administrateur'),
    path('Diacre/Comite/<int:cle>/', Comite_quartier, name='Comite_quartier'),
    path('Diacre/Ajouter_comite/<int:cle>/', Ajouter_comite, name='Ajouter_comite'),
    path('Diacre/Modifier_comite/<int:cle>/', Modifier_comite, name='Modifier_comite'),
    path('Diacre/Supprimer_Menbre_comite/<int:cle>/', Supprimer_Menbre_comite, name='Supprimer_Menbre_comite'),
    path('Diacre/Evenement', Evenements, name='Evenement'),
    path('Diacre/Detail_evenement/<int:cle>/', Detail_Evenements, name='Detail_Evenements'),






]
