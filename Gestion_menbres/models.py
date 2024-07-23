from django import forms
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Quartier(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    delimitation = models.TextField(verbose_name="Limitations du quartier")

    def __str__(self):
        return str(self.nom)


class Fonction(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255, verbose_name="Nom")

    def __str__(self):
        return f"{self.nom}"


class Menbres(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255, blank=False)
    postnom = models.CharField(max_length=255, blank=False)
    prenom = models.CharField(max_length=255, blank=False)
    date = models.DateField()
    GENRE_CHOICES = [
        ('Masculin', 'Masculin'),
        ('Féminin', 'Féminin'),
    ]
    genre = models.CharField(max_length=255, choices=GENRE_CHOICES, blank=False)
    Adresse = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=255, blank=False)
    STATUT_CHOICES = [
        ('Actif', 'Actif'),
        ('Inactif', 'Inactif'),

    ]
    statut = models.CharField(max_length=255, blank=False, choices=STATUT_CHOICES, verbose_name="Statut")
    Etat_CHOICES = [
        ('Célibataire', 'Célibataire'),
        ('Marié(e)', 'Marié(e)'),
        ('Divorcé(e)', 'Divorcé(e)'),
        ('Veuf/Veuve', 'Veuf/Veuve'),

    ]
    etat_civil = models.CharField(max_length=255, blank=False,choices=Etat_CHOICES, verbose_name="Etat civil")
    photo = models.ImageField(blank=True, upload_to='images')
    quartier = models.ForeignKey(Quartier, on_delete=models.CASCADE, verbose_name="Quartier")
    SANG_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    groupe_sanguin = models.CharField(max_length=255, blank=False, verbose_name="Groupe sanguin", choices=SANG_CHOICES)
    fonction = models.ForeignKey(Fonction, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Menbre"
        verbose_name_plural = "Menbres"

    def __str__(self):
        return f"{self.nom} {self.postnom} {self.prenom}"


class Comite(models.Model):
    quartier = models.ForeignKey(Quartier, on_delete=models.CASCADE, verbose_name="Quartier")
    menbre = models.OneToOneField(Menbres, on_delete=models.CASCADE, verbose_name="Membre")
    Fonction_CHOICES = [
        ('Président', 'Président'),
        ('Vice-président', 'Vice-président'),
        ('Collecteur', 'Collecteur'),
    ]
    fonction = models.CharField(max_length=255, blank=False, verbose_name="Fonction", choices=Fonction_CHOICES)

    def __str__(self):
        return f"{self.menbre} | {self.fonction} | {self.quartier.nom}"


class Communication(models.Model):
    id = models.AutoField(primary_key=True)
    type_comm = models.CharField(max_length=255, blank=False, verbose_name="Type de communication")
    contenu = models.TextField(verbose_name="Contenu")
    date_comm = models.DateField(verbose_name="Date")
    destinataire = models.ForeignKey(Menbres, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type_comm}"


class Evenement(models.Model):
    id = models.AutoField(primary_key=True)
    type_even = models.CharField(max_length=255, blank=False,verbose_name="Type d'événement")
    date_even = models.DateField(verbose_name="Date")
    heure_even = models.TimeField(verbose_name="Heure")
    place_even = models.CharField(max_length=255, blank=False, verbose_name="Lieu")
    membres = models.ManyToManyField(Menbres, related_name='Evenement_membres',blank=True, null=True)

    def __str__(self):
        return f"{self.type_even}"


class Activite(models.Model):
    id = models.AutoField(primary_key=True)
    type_activ = models.CharField(max_length=255, blank=False, verbose_name="Type d'activité")
    date_activ = models.DateField(verbose_name="Date")
    place_activ = models.CharField(max_length=255, blank=False, verbose_name="Place")
    membres = models.ManyToManyField(Menbres, related_name='Activite_membres')

    def __str__(self):
        return f"{self.type_activ}"


class Offrande(models.Model):
    id = models.AutoField(primary_key=True)
    type_off = models.CharField(max_length=255, blank=False, verbose_name="Type d'offrande")
    montant = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant")
    date_off = models.DateField(verbose_name="Date")
    menbre = models.ForeignKey(Menbres, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type_off}"


class Administateur(models.Model):
    id = models.AutoField(primary_key=True)
    id_menbre = models.ForeignKey(Menbres, on_delete=models.CASCADE, verbose_name="Menbre")
    profession = models.CharField(max_length=255, blank=False, verbose_name="Profession")
    debut_mandat = models.DateField(verbose_name="Debut mandat")
    fin_mandat = models.DateField(verbose_name="Fin mandat")
    ETAT_MANDAT_CHOICES = [
        ('En cours', 'En cours'),
        ('Terminé', 'Terminé'),
        ('Annulé', 'Annulé'),
        ('Suspendu', 'Suspendu'),
        ('Autre', 'Autre'),
    ]
    etat_mandat = models.CharField(max_length=255, blank=False, choices=ETAT_MANDAT_CHOICES, verbose_name="Etat mandat")

    def __str__(self):
        return f"{self.id_menbre.nom} {self.id_menbre.postnom} {self.id_menbre.prenom}"


class Diacre(models.Model):
    id = models.AutoField(primary_key=True)
    id_menbre = models.ForeignKey(Menbres, on_delete=models.CASCADE, verbose_name="Menbre")
    profession = models.CharField(max_length=255, blank=False, verbose_name="Profession")
    debut_mandat = models.DateField(verbose_name="Début mandat")
    fin_mandat = models.DateField(verbose_name="Fin mandat")
    ETAT_MANDAT_CHOICES = [
        ('En cour', 'En cours'),
        ('Terminé', 'Terminé'),
        ('Annulé', 'Annulé'),
        ('Suspendu', 'Suspendu'),
        ('Autre', 'Autre'),
    ]
    etat_mandat = models.CharField(max_length=255, blank=False, choices=ETAT_MANDAT_CHOICES)

    def __str__(self):
        return f"{self.id_menbre.nom} {self.id_menbre.postnom} {self.id_menbre.prenom}"


class Pasteur(models.Model):
    id = models.AutoField(primary_key=True)
    id_menbre = models.ForeignKey(Menbres, on_delete=models.CASCADE, verbose_name="Menbre")
    ETAT_FONCTION = [
        ('P', 'Principal'),
        ('A', 'Associé'),

    ]
    fonction = models.CharField(max_length=255, blank=False, choices=ETAT_FONCTION)

    def __str__(self):
        return f"{self.id_menbre.nom} {self.id_menbre.postnom} {self.id_menbre.prenom}"


class Technique(models.Model):
    id = models.AutoField(primary_key=True)
    id_menbre = models.ForeignKey(Menbres, on_delete=models.CASCADE,verbose_name="Menbre")
    departement = models.CharField(max_length=255, blank=False, verbose_name="Département")

    def __str__(self):
        return f"{self.id_menbre.nom} {self.id_menbre.postnom} {self.id_menbre.prenom}"


class Besoin(models.Model):
    id = models.AutoField(primary_key=True)
    materiel = models.TextField(verbose_name="Démande")
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(verbose_name="Prix")
    technicien = models.ForeignKey(Technique, on_delete=models.CASCADE, verbose_name="Téchnicien")
    destinateur = models.CharField(max_length=255, blank=False, verbose_name="Destinataire")

    def __str__(self):
        return f"{self.technicien.departement}"


class JourSemaine(models.Model):
    JOUR_SEMAINE_CHOICES = [
        ('lundi', 'Lundi'),
        ('mardi', 'Mardi'),
        ('mercredi', 'Mercredi'),
        ('jeudi', 'Jeudi'),
        ('vendredi', 'Vendredi'),
        ('samedi', 'Samedi'),
        ('dimanche', 'Dimanche'),
    ]
    jour = models.CharField(max_length=10, choices=JOUR_SEMAINE_CHOICES)

    def __str__(self):
        return self.jour


class Garde(models.Model):
    id = models.AutoField(primary_key=True)
    id_menbre = models.ForeignKey(Menbres, on_delete=models.CASCADE, verbose_name="Menbre")
    profession = models.CharField(max_length=255, blank=False, verbose_name="Profession")

    emploi_temps = models.ManyToManyField('JourSemaine', verbose_name='Emploi du temps')

    STATUT_CHOICES = [
        ('A', 'Ancien'),
        ('N', 'Nouveau'),
        ('O', 'Autre'),
    ]
    statut = models.CharField(max_length=255, blank=False, choices=STATUT_CHOICES)
    GRADE_CHOICES = [
        ('secretaire', 'Secrétaire'),
        ('disciplinaire', 'Disciplinaire'),
        ('commandant', 'Commandant'),
    ]
    grade = models.CharField(max_length=255, blank=False, verbose_name="Grade", choices=GRADE_CHOICES)
    date_recrutement = models.DateField(verbose_name="Date de récrutement")

    def __str__(self):
        return f"{self.id_menbre.nom} {self.id_menbre.postnom} {self.id_menbre.prenom}"


class Gardinage(models.Model):
    garde = models.ForeignKey(Menbres, on_delete=models.CASCADE, related_name='Garde')
    membre = models.ForeignKey(Menbres, on_delete=models.CASCADE, verbose_name="Menbre")
    date = models.DateField(verbose_name="Date")
    heure_arrive = models.TimeField(verbose_name="Heure d'arrivée")
    heure_depart = models.TimeField(verbose_name="Heure de départ")
    remarque = models.TextField(verbose_name="Remarques")

    def __str__(self):
        return f"{self.garde}"


