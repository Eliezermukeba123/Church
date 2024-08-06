from django.contrib.auth.decorators import login_required
from django.urls import path

from .AdminViews import Admin_view, culte_consultation_admin, vue_culte_admin, Modifier_culte_admin
from .views import Page_acceuil, login_view, Pasteur_view, Menbres_view, Detail_membre, logout_view, Diacre_view, \
    Menbres_diacre_view, Detail_membre_diacre, Ajouter_membre_diacre, Modifier_menbre, Quartier_view, \
    Supprimer_Quartier, Modifier_Quartier, Fonction_view, Modifier_Fonction, Supprimer_Fonction, Diacres_view, \
    Ajouter_diacre, Modifier_diacres, Administrateur_view, Ajouter_administrateur, Modifier_administrateur, \
    Comite_quartier, Ajouter_comite, Modifier_comite, Supprimer_Menbre_comite, Evenements, Detail_Evenements, culte, \
    culte_create, culte_consultation, vue_culte, Modifier_culte, delete_culte, culte_consultation_pasteur, \
    vue_culte_pasteur, Modifier_culte_pasteur, delete_event, delete_membre

app_name = 'gestMenb'
urlpatterns = [
    # Admin system -------------------------------------------------------------------------------------

    path('', login_view, name='login_view'),
    path('logout/', logout_view, name='logout'),
    path('Home', Page_acceuil, name='Page_acceuil'),

    # PASTEUR
    path('Pasteur', Pasteur_view, name='Pasteur_view'),
    path('membres', Menbres_view, name='Menbres_view'),
    path('Detail_membre/<int:cle>/', Detail_membre, name='Detail_membre'),
    path('Pasteur/culte_consultation', culte_consultation_pasteur, name='culte_consultation_pasteur'),
    path('Pasteur/Culte/<int:cle>/', vue_culte_pasteur, name='vue_culte_pasteur'),
    path('Pasteur/Culte_Modifie/<int:cle>/', Modifier_culte_pasteur, name='Modifier_culte_pasteur'),

    # Diacre
    path('Diacre', Diacre_view, name='Diacre_view'),
    path('Diacre/Membres', Menbres_diacre_view, name='Menbres_diacre_view'),
    path('Diacre/Detail_membre/<int:cle>/', Detail_membre_diacre, name='Detail_membre_diacre'),
    path('Diacre/Culte_Membre/<int:cle>/', delete_membre, name='delete_membre'),
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
    path('Diacre/Culte_Evenement/<int:cle>/', delete_event, name='delete_event'),
    path('Diacre/Culte', culte, name='culte'),
    path('Diacre/Démarrer_culte', culte_create, name='culte_create'),
    path('Diacre/Consulter_culte', culte_consultation, name='culte_consultation'),
    path('Diacre/Culte/<int:cle>/', vue_culte, name='vue_culte'),
    path('Diacre/Culte_Modifie/<int:cle>/', Modifier_culte, name='Modifier_culte'),
    path('Diacre/Culte_Supprimer/<int:cle>/', delete_culte, name='delete_culte'),

    # Administrateur
    path('Administrateur', Admin_view, name='Admin_view'),
    path('Administrateur/Cultes', culte_consultation_admin, name='culte_consultation_admin'),
    path('Administrateur/Culte/<int:cle>/', vue_culte_admin, name='vue_culte_admin'),
    path('Administrateur/Culte_Modifier/<int:cle>/', Modifier_culte_admin, name='Modifier_culte_admin'),




]
