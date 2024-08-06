from datetime import date

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.


# LOGIN ------------

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils import timezone
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt

from .filters import OrderFilter, QuartierFilter, FonctionFilter, DiacreFilter, AdministateurFilter, EvenementFilter, \
    CulteFilter
from .forms import UserLoginForm, MenbresForm, QuartierForm, FonctionForm, DiacreForm, AdministateurForm, ComiteForm, \
    EvenementForm, CulteForm
from django.urls import reverse

from .models import Menbres, Quartier, Evenement, Fonction, Diacre, Administateur, Comite, Culte


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.groups.filter(name='pasteur').exists():
                    login(request, user)
                    return redirect('gestMenb:Pasteur_view')

                if user.groups.filter(name='diacre').exists():
                    login(request, user)
                    return redirect('gestMenb:Diacre_view')
                if user.groups.filter(name='administrateur').exists():
                    login(request, user)
                    return redirect('gestMenb:Admin_view')
            else:
                messages.error(request, "Les informations d'identification sont incorrectes.")

                return redirect('gestMenb:login_view')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('gestMenb:login_view')


def nombre_mois_membre(year):
    January = Culte.objects.filter(date__year=year, date__month=1).aggregate(total=Sum('nombre_membres'))['total']
    February = Culte.objects.filter(date__year=year, date__month=2).aggregate(total=Sum('nombre_membres'))['total']
    March = Culte.objects.filter(date__year=year, date__month=3).aggregate(total=Sum('nombre_membres'))['total']
    April = Culte.objects.filter(date__year=year, date__month=4).aggregate(total=Sum('nombre_membres'))['total']
    May = Culte.objects.filter(date__year=year, date__month=5).aggregate(total=Sum('nombre_membres'))['total']
    June = Culte.objects.filter(date__year=year, date__month=6).aggregate(total=Sum('nombre_membres'))['total']
    July = Culte.objects.filter(date__year=year, date__month=7).aggregate(total=Sum('nombre_membres'))['total']
    August = Culte.objects.filter(date__year=year, date__month=8).aggregate(total=Sum('nombre_membres'))['total']
    September = Culte.objects.filter(date__year=year, date__month=9).aggregate(total=Sum('nombre_membres'))['total']
    October = Culte.objects.filter(date__year=year, date__month=10).aggregate(total=Sum('nombre_membres'))['total']
    November = Culte.objects.filter(date__year=year, date__month=11).aggregate(total=Sum('nombre_membres'))['total']
    December = Culte.objects.filter(date__year=year, date__month=12).aggregate(total=Sum('nombre_membres'))['total']
    JanuaryO = Culte.objects.filter(date__year=year, date__month=1).aggregate(total=Sum('nombre_offrandes'))['total']
    FebruaryO = Culte.objects.filter(date__year=year, date__month=2).aggregate(total=Sum('nombre_offrandes'))['total']
    MarchO = Culte.objects.filter(date__year=year, date__month=3).aggregate(total=Sum('nombre_offrandes'))['total']
    AprilO = Culte.objects.filter(date__year=year, date__month=4).aggregate(total=Sum('nombre_offrandes'))['total']
    MayO = Culte.objects.filter(date__year=year, date__month=5).aggregate(total=Sum('nombre_offrandes'))['total']
    JuneO = Culte.objects.filter(date__year=year, date__month=6).aggregate(total=Sum('nombre_offrandes'))['total']
    JulyO = Culte.objects.filter(date__year=year, date__month=7).aggregate(total=Sum('nombre_offrandes'))['total']
    AugustO = Culte.objects.filter(date__year=year, date__month=8).aggregate(total=Sum('nombre_offrandes'))['total']
    SeptemberO = Culte.objects.filter(date__year=year, date__month=9).aggregate(total=Sum('nombre_offrandes'))['total']
    OctoberO = Culte.objects.filter(date__year=year, date__month=10).aggregate(total=Sum('nombre_offrandes'))['total']
    NovemberO = Culte.objects.filter(date__year=year, date__month=11).aggregate(total=Sum('nombre_offrandes'))['total']
    DecemberO = Culte.objects.filter(date__year=year, date__month=12).aggregate(total=Sum('nombre_offrandes'))['total']
    return January, February, March, April, May, June, July, August, September, October, November, December, JanuaryO, FebruaryO, MarchO, AprilO, MayO, JuneO, JulyO, AugustO, SeptemberO, OctoberO, NovemberO, DecemberO


@login_required(login_url='gestMenb:login_view')
def Page_acceuil(request):
    return render(request, "acceuil/page_acceuil.html")


@login_required(login_url='gestMenb:login_view')
def Pasteur_view(request):
    membres = Menbres.objects.all().count()
    culte= Culte.objects.latest('id')
    offrande = culte.nombre_offrandes
    offrande_const  = culte.nombre_construction

    actuel = timezone.now()
    current_year = actuel.year
    current_month = actuel.month
    events = Evenement.objects.filter(date_even__year=current_year, date_even__month=current_month).count()
    January, February, March, April, May, June, July, August, September, October, November, December, JanuaryO, FebruaryO, MarchO, AprilO, MayO, JuneO, JulyO, AugustO, SeptemberO, OctoberO, NovemberO, DecemberO = nombre_mois_membre(current_year)

    if membres == 0:
        pourcentage_homme = 50
        pourcentage_femme = 50
    else:

        # Récupération du nombre d'hommes et de femmes
        homme_count = Menbres.objects.filter(genre='Masculin').count()
        femme_count = Menbres.objects.filter(genre='Féminin').count()

        # Calcul des pourcentages
        pourcentage_homme = (homme_count / membres) * 100
        pourcentage_femme = (femme_count / membres) * 100

    return render(request, "pasteur/dashboard.html", context={"membres": membres, "events": events,
                                                              "pourcentage_homme": pourcentage_homme,
                                                              "pourcentage_femme": pourcentage_femme,
                                                              "January": January,
                                                              "February": February, "March": March, "April": April,
                                                              "May": May, "June": June, "July": July, "August": August,
                                                              "September": September, "October": October,
                                                              "November": November, "December": December,
                                                              "JanuaryO": JanuaryO,
                                                              "FebruaryO": FebruaryO, "MarchO": MarchO, "AprilO": AprilO,
                                                              "MayO": MayO, "JuneO": JuneO, "JulyO": JulyO, "AugustO": AugustO,
                                                              "SeptemberO": SeptemberO, "OctoberO": OctoberO,
                                                              "NovemberO": NovemberO, "DecemberO": DecemberO,
                                                              "offrande" : offrande, "offrande_const":offrande_const
                                                              })


@login_required(login_url='gestMenb:login_view')
def Menbres_view(request):
    list_menbres = Menbres.objects.order_by('id')

    myFilter = OrderFilter(request.GET, queryset=list_menbres)
    filtered_menbres = myFilter.qs
    nombre = filtered_menbres.count()
    paginator = Paginator(filtered_menbres, 20)  # Paginer les objets avec 10 objets par page
    page = request.GET.get('page')
    objets_page = paginator.get_page(page)
    list_quartier = Quartier.objects.all()
    return render(request, "pasteur/menbres.html", context={"objets_page": objets_page,
                                                            "nombre": nombre,
                                                            "list_quartier": list_quartier, "myFilter": myFilter})


@login_required(login_url='gestMenb:login_view')
def Detail_membre(request, cle):
    menbre = Menbres.objects.get(id=cle)
    return render(request, "pasteur/membres_detail.html", context={"menbre": menbre})


@login_required(login_url='gestMenb:login_view')
def culte_consultation_pasteur(request):
    list_cultes = Culte.objects.order_by('-id')
    myFilter = CulteFilter(request.GET, queryset=list_cultes)
    filtered_cultes = myFilter.qs
    nombre = filtered_cultes.count()
    paginator = Paginator(filtered_cultes, 10)  # Paginer les objets avec 10 objets par page
    page = request.GET.get('page')
    objets_page = paginator.get_page(page)
    date_actuelle = date.today()

    return render(request, 'pasteur/consulter_culte.html', context={"objets_page": objets_page,
                                                                    "nombre": nombre,
                                                                    "myFilter": myFilter,
                                                                    "date_actuelle": date_actuelle})


@login_required(login_url='gestMenb:login_view')
def vue_culte_pasteur(request, cle):
    date_actuelle = date.today()
    culte = Culte.objects.get(id=cle)
    date_culte = culte.date
    heure_d = culte.heure_debut
    heure_f = culte.heure_fin
    effectif = culte.nombre_membres
    communiquer = culte.communication
    temoinage = culte.temoignages_du_jour
    cantiques = culte.cantiques_speciaux
    anniversaire = culte.anniversaire
    consecration = culte.consecration
    remerciement = culte.remerciement
    predicateur = culte.predicateur
    regulier = culte.nombre_offrandes
    construction = culte.nombre_construction
    if predicateur:
        predic = predicateur
    else:
        predic = culte.predicateur_visiteur

    return render(request, 'pasteur/vue_culte.html',
                  context={"date_culte": date_culte, "predicateur": predic, "heure_d": heure_d, "heure_f": heure_f,
                           "effectif": effectif, "communiquer": communiquer, "temoinage": temoinage,
                           "cantiques": cantiques, "anniversaire": anniversaire, "consecration": consecration,
                           "remerciement": remerciement, "date_actuelle": date_actuelle, "cle": cle,
                           "regulier": regulier, "construction": construction})


@login_required(login_url='gestMenb:login_view')
def Modifier_culte_pasteur(request, cle):
    culte = Culte.objects.get(id=cle)
    date_culte = culte.date
    date = culte.date
    if request.method == 'POST':
        form = CulteForm(request.POST, instance=culte)
        if form.is_valid():
            form.save()
            messages.success(request, f'Le culte du {date} a été modifié!')
            return redirect('gestMenb:culte_consultation_pasteur')

        else:
            print(form.errors)
            messages.error(request, "Une erreur est survenue lors de la mise à jour.")
            return redirect('gestMenb:Modifier_culte_pasteur', cle=cle)
    else:
        form = CulteForm(instance=culte)
        return render(request, 'pasteur/modifier_culte.html',
                      context={"form": form, "date_culte": date_culte})


# DIACRE ---------------------------------------------------------------------------- PRINCIPAL


@login_required(login_url='gestMenb:login_view')
def Diacre_view(request):
    membres = Menbres.objects.all().count()
    actuel = timezone.now()
    current_year = actuel.year
    current_month = actuel.month
    events = Evenement.objects.filter(date_even__year=current_year, date_even__month=current_month).count()
    January, February, March, April, May, June, July, August, September, October, November, December, JanuaryO, FebruaryO, MarchO, AprilO, MayO, JuneO, JulyO, AugustO, SeptemberO, OctoberO, NovemberO, DecemberO = nombre_mois_membre(
        current_year)

    if membres == 0:
        pourcentage_homme = 50
        pourcentage_femme = 50
    else:

        # Récupération du nombre d'hommes et de femmes
        homme_count = Menbres.objects.filter(genre='Masculin').count()
        femme_count = Menbres.objects.filter(genre='Féminin').count()

        # Calcul des pourcentages
        pourcentage_homme = (homme_count / membres) * 100
        pourcentage_femme = (femme_count / membres) * 100

    return render(request, "diacre/dashboard.html", context={"membres": membres, "events": events,
                                                             "pourcentage_homme": pourcentage_homme,
                                                             "pourcentage_femme": pourcentage_femme, "January": January,
                                                             "February": February, "March": March, "April": April,
                                                             "May": May, "June": June, "July": July, "August": August,
                                                             "September": September, "October": October,
                                                             "November": November, "December": December})


@login_required(login_url='gestMenb:login_view')
def Menbres_diacre_view(request):
    list_menbres = Menbres.objects.order_by('id')
    myFilter = OrderFilter(request.GET, queryset=list_menbres)
    filtered_menbres = myFilter.qs
    nombre = filtered_menbres.count()
    paginator = Paginator(filtered_menbres, 20)  # Paginer les objets avec 10 objets par page
    page = request.GET.get('page')
    objets_page = paginator.get_page(page)
    list_quartier = Quartier.objects.all()
    return render(request, "diacre/menbres.html", context={"objets_page": objets_page,
                                                           "nombre": nombre, "list_quartier": list_quartier,
                                                           "myFilter": myFilter})


@login_required(login_url='gestMenb:login_view')
def Detail_membre_diacre(request, cle):
    menbre = Menbres.objects.get(id=cle)
    return render(request, "diacre/membres_detail.html", context={"menbre": menbre})


@login_required(login_url='gestMenb:login_view')
@csrf_exempt
def delete_membre(request, cle):
    try:
        membre = Menbres.objects.get(id=cle)
        membre.delete()
        return JsonResponse({'status': 'success'})
    except Evenement.DoesNotExist:
        return JsonResponse({'status': 'fail', 'message': 'Item not found'}, status=404)


@login_required(login_url='gestMenb:login_view')
def Ajouter_membre_diacre(request):
    if request.method == 'POST':
        form = MenbresForm(request.POST, request.FILES)
        if form.is_valid():
            telephone = form.cleaned_data['telephone']
            if Menbres.objects.filter(telephone=telephone).exists():
                # Le membre existe déjà, ajoutez un message d'erreur
                messages.error(request, 'Un membre avec ce numéro de téléphone existe déjà .')
                return render(request, 'diacre/ajouter_membre.html',
                              {'form': form, 'messages': messages.get_messages(request)})
            else:
                # Le membre n'existe pas, enregistrez-le
                form.save()
                messages.success(request, 'success')

                return redirect('gestMenb:Menbres_diacre_view')
        else:
            messages.error(request, "Une erreur est survenue lors de l'enregistrement du membre, Veuillez remplir "
                                    "tous les champs.")
            return render(request, 'diacre/ajouter_membre.html',
                          {'form': form, 'messages': messages.get_messages(request)})
    else:
        form = MenbresForm()

    return render(request, "diacre/ajouter_membre.html", context={"form": form})


@login_required(login_url='gestMenb:login_view')
def Modifier_menbre(request, cle):
    membre = Menbres.objects.get(id=cle)
    if request.method == 'POST':
        form = MenbresForm(request.POST, request.FILES, instance=membre)
        if form.is_valid():
            form.save()
            messages.success(request, "Le membre a été mis à jour avec succès.")
            return redirect('gestMenb:Detail_membre_diacre', cle=cle)
        else:
            messages.error(request, "Une erreur est survenue lors de la mise à jour du membre.")
            return redirect('gestMenb:Detail_membre_diacre', cle=cle)
    else:
        form = MenbresForm(instance=membre)
    return render(request, 'diacre/modifie_membre.html', context={"form": form})


@login_required(login_url='gestMenb:login_view')
def Quartier_view(request):
    quartiers = Quartier.objects.all()
    myFilter = QuartierFilter(request.GET, queryset=quartiers)
    filtered_menbres = myFilter.qs
    quartier_number = quartiers.count()
    if request.method == 'POST':
        form = QuartierForm(request.POST)
        if form.is_valid():
            nom_quartier = form.cleaned_data['nom']
            if Quartier.objects.filter(nom=nom_quartier).exists():
                messages.error(request, "Ce quartier existe déjà.")
                return redirect('gestMenb:Quartier_view')
            form.save()
            messages.success(request, "Le quartier a été ajouter avec succès.")
            return redirect('gestMenb:Quartier_view')
    else:
        form = QuartierForm()
    return render(request, "diacre/quartier.html",
                  {'form': form, "quartiers": quartiers, "quartier_number": quartier_number, "myFilter": myFilter,
                   "filtered_menbres": filtered_menbres})


@login_required(login_url='gestMenb:login_view')
def Supprimer_Quartier(request, cle):
    try:
        quartier = Quartier.objects.get(id=cle)
    except Quartier.DoesNotExist:
        messages.error(request, "Le quartier que vous essayez de supprimer n'existe pas.")
        return redirect('gestMenb:Quartier_view')

    if request.method == 'POST':
        quartier.delete()
        messages.success(request, "Le quartier  a été supprimée avec succès.")
        return redirect('gestMenb:Quartier_view')
    return render(request, 'diacre/supprimer_Quartier.html', context={"cle": cle})


@login_required(login_url='gestMenb:login_view')
def Modifier_Quartier(request, cle):
    quartier = Quartier.objects.get(id=cle)
    if request.method == 'POST':
        form = QuartierForm(request.POST, instance=quartier)
        if form.is_valid():
            nouveau_nom = form.cleaned_data['nom']
            if Quartier.objects.exclude(id=quartier.id).filter(nom=nouveau_nom).exists():
                messages.error(request, "Ce nom de quartier existe déjà.")
                return render(request, 'diacre/modifier_quartier.html', context={"form": form, "nom": quartier.nom})
            form.save()
            messages.success(request, "Le quartier a été mis à jour avec succès.")
            return redirect('gestMenb:Quartier_view')
        else:
            messages.error(request, "Une erreur est survenue lors de la mise à jour du quartier.")
            return redirect('gestMenb:Modifier_Quartier', cle=cle)
    else:
        form = QuartierForm(instance=quartier)
        return render(request, 'diacre/modifier_quartier.html', context={"form": form, "nom": quartier.nom})


@login_required(login_url='gestMenb:login_view')
def Fonction_view(request):
    fonctions = Fonction.objects.all()
    myFilter = FonctionFilter(request.GET, queryset=fonctions)
    filtered_menbres = myFilter.qs
    fonction_number = fonctions.count()
    if request.method == 'POST':
        form = FonctionForm(request.POST)
        if form.is_valid():
            nom_fonction = form.cleaned_data['nom']
            if Fonction.objects.filter(nom=nom_fonction).exists():
                messages.error(request, "Cette fonction existe déjà.")
                return redirect('gestMenb:Fonction_view')
            form.save()
            messages.success(request, "La fonction a été ajoutée avec succès.")
            return redirect('gestMenb:Fonction_view')
    else:
        form = FonctionForm()
    return render(request, "diacre/fonctions.html",
                  {'form': form, "fonctions": fonctions, "fonction_number": fonction_number, "myFilter": myFilter,
                   "filtered_menbres": filtered_menbres})


@login_required(login_url='gestMenb:login_view')
def Modifier_Fonction(request, cle):
    fonction = Fonction.objects.get(id=cle)
    if request.method == 'POST':
        form = FonctionForm(request.POST, instance=fonction)
        if form.is_valid():
            nouveau_nom = form.cleaned_data['nom']
            if Fonction.objects.exclude(id=fonction.id).filter(nom=nouveau_nom).exists():
                messages.error(request, "Ce nom de fonction existe déjà.")
                return render(request, 'diacre/modifier_fonction.html', context={"form": form, "nom": fonction.nom})
            form.save()
            messages.success(request, "La fonction a été mise à jour avec succès.")
            return redirect('gestMenb:Fonction_view')
        else:
            messages.error(request, "Une erreur est survenue lors de la mise à jour de la fonction.")
            return redirect('gestMenb:Modifier_Fonction', cle=cle)
    else:
        form = FonctionForm(instance=fonction)
        return render(request, 'diacre/modifier_fonction.html', context={"form": form, "nom": fonction.nom})


@login_required(login_url='gestMenb:login_view')
def Supprimer_Fonction(request, cle):
    try:
        fonction = Fonction.objects.get(id=cle)
    except Fonction.DoesNotExist:
        messages.error(request, "La fonction que vous essayez de supprimer n'existe pas.")
        return redirect('gestMenb:Fonction_view')

    if request.method == 'POST':
        fonction.delete()
        messages.success(request, "La fonction a été supprimée avec succès.")
        return redirect('gestMenb:Fonction_view')
    return render(request, 'diacre/supprimer_Fonction.html', context={"cle": cle})


@login_required(login_url='gestMenb:login_view')
def Diacres_view(request):
    diacres = Diacre.objects.all()
    myFilter = DiacreFilter(request.GET, queryset=diacres)
    filtered_menbres = myFilter.qs
    nombre = filtered_menbres.count()
    paginator = Paginator(filtered_menbres, 10)  # Paginer les objets avec 10 objets par page
    page = request.GET.get('page')
    objets_page = paginator.get_page(page)
    list_quartier = Quartier.objects.all()
    return render(request, "diacre/diacres.html", context={"objets_page": objets_page,
                                                           "nombre": nombre,
                                                           "list_quartier": list_quartier, "myFilter": myFilter})


@login_required(login_url='gestMenb:login_view')
def Ajouter_diacre(request):
    if request.method == 'POST':
        form = DiacreForm(request.POST, request.FILES)
        if form.is_valid():
            id_menbre = form.cleaned_data['id_menbre']

            if Diacre.objects.filter(id_menbre=id_menbre).exists():
                # Le membre existe déjà, ajoutez un message d'erreur
                messages.error(request, 'Ce diacre existe déjà .')
                return render(request, 'diacre/ajouter_diacre.html',
                              {'form': form, 'messages': messages.get_messages(request)})
            else:
                # Le membre n'existe pas, enregistrez-le
                form.save()

                messages.success(request, 'Un diacre a été ajouté !')
                return redirect('gestMenb:Diacres_view')
        else:
            messages.error(request, "Une erreur est survenue lors de l'enregistrement du membre, Veuillez remplir "
                                    "tous les champs.")
            return render(request, 'diacre/ajouter_diacre.html',
                          {'form': form, 'messages': messages.get_messages(request)})
    else:
        form = DiacreForm()

    return render(request, "diacre/ajouter_diacre.html", context={"form": form})


@login_required(login_url='gestMenb:login_view')
def Modifier_diacres(request, cle):
    diacre = Diacre.objects.get(id=cle)
    if request.method == 'POST':
        form = DiacreForm(request.POST, instance=diacre)
        if form.is_valid():
            id_menbre = form.cleaned_data['id_menbre']

            if Diacre.objects.exclude(id=form.instance.id).filter(id_menbre=id_menbre).exists():
                # Le membre existe déjà, ajoutez un message d'erreur
                messages.error(request, 'Ce diacre existe déjà .')
                return render(request, 'diacre/modifier_diacre.html',
                              {'form': form, 'messages': messages.get_messages(request)})
            else:
                # Le membre n'existe pas, enregistrez-le
                form.save()
                messages.success(request, 'La diacre été modifié !')

                return redirect('gestMenb:Diacres_view')

        else:
            messages.error(request, "Une erreur est survenue lors de la mise à jour du diacre.")
            return redirect('gestMenb:Modifier_diacres', cle=cle)
    else:
        form = DiacreForm(instance=diacre)
        return render(request, 'diacre/modifier_diacre.html', context={"form": form})


@login_required(login_url='gestMenb:login_view')
def Administrateur_view(request):
    administrateurs = Administateur.objects.all()
    myFilter = AdministateurFilter(request.GET, queryset=administrateurs)
    filtered_menbres = myFilter.qs
    nombre = filtered_menbres.count()
    paginator = Paginator(filtered_menbres, 10)  # Paginer les objets avec 10 objets par page
    page = request.GET.get('page')
    objets_page = paginator.get_page(page)
    return render(request, "diacre/administrateur.html", context={"objets_page": objets_page,
                                                                  "nombre": nombre, "myFilter": myFilter})


@login_required(login_url='gestMenb:login_view')
def Ajouter_administrateur(request):
    if request.method == 'POST':
        form = AdministateurForm(request.POST, request.FILES)
        if form.is_valid():
            id_menbre = form.cleaned_data['id_menbre']

            if Administateur.objects.filter(id_menbre=id_menbre).exists():
                # Le membre existe déjà, ajoutez un message d'erreur
                messages.error(request, 'Cet administrateur existe déjà .')
                return render(request, 'diacre/ajouter_administrateur.html',
                              {'form': form, 'messages': messages.get_messages(request)})
            else:
                # Le membre n'existe pas, enregistrez-le
                form.save()
                messages.success(request, 'Un administrateur a été ajouté !')

                return redirect('gestMenb:Administrateur_view')
        else:
            messages.error(request, "Une erreur est survenue lors de l'enregistrement du membre, Veuillez remplir "
                                    "tous les champs.")
            return render(request, 'diacre/ajouter_administrateur.html',
                          {'form': form, 'messages': messages.get_messages(request)})
    else:
        form = AdministateurForm()

    return render(request, "diacre/ajouter_administrateur.html", context={"form": form})


@login_required(login_url='gestMenb:login_view')
def Modifier_administrateur(request, cle):
    administrateur = Administateur.objects.get(id=cle)
    if request.method == 'POST':
        form = AdministateurForm(request.POST, instance=administrateur)
        if form.is_valid():
            id_menbre = form.cleaned_data['id_menbre']

            if Administateur.objects.exclude(id=form.instance.id).filter(id_menbre=id_menbre).exists():
                # Le membre existe déjà, ajoutez un message d'erreur
                messages.error(request, 'Cet administrateur  existe déjà .')
                return render(request, 'diacre/modifier_administrateur.html',
                              {'form': form, 'messages': messages.get_messages(request)})
            else:
                # Le membre n'existe pas, enregistrez-le
                form.save()
                messages.success(request, 'Administrateur  modifié avec succès !')

                return redirect('gestMenb:Administrateur_view')

        else:
            messages.error(request, "Une erreur est survenue lors de la mise à jour de l'administrateur.")
            return redirect('gestMenb:Modifier_administrateur', cle=cle)
    else:
        form = AdministateurForm(instance=administrateur)
        return render(request, 'diacre/modifier_administrateur.html', context={"form": form})


@login_required(login_url='gestMenb:login_view')
def Comite_view(request):
    comites = Comite.objects.all()
    myFilter = AdministateurFilter(request.GET, queryset=comites)
    filtered_menbres = myFilter.qs
    nombre = filtered_menbres.count()
    paginator = Paginator(filtered_menbres, 2)  # Paginer les objets avec 10 objets par page
    page = request.GET.get('page')
    objets_page = paginator.get_page(page)
    return render(request, "diacre/administrateur.html", context={"objets_page": objets_page,
                                                                  "nombre": nombre, "myFilter": myFilter})


@login_required(login_url='gestMenb:login_view')
def Comite_quartier(request, cle):
    quartier = Quartier.objects.get(id=cle)
    quartier_nom = quartier.nom
    if Comite.objects.filter(quartier=quartier).exists():
        objets_page = Comite.objects.filter(quartier=quartier)
        return render(request, "diacre/comites.html",
                      context={"objets_page": objets_page, "quartier_nom": quartier_nom, "cle": cle})
    else:
        return render(request, "diacre/comite.html", context={"cle": cle, "quartier_nom": quartier_nom})


@login_required(login_url='gestMenb:login_view')
def Ajouter_comite(request, cle):
    quartier_instance = Quartier.objects.get(id=cle)

    if request.method == 'POST':
        form = ComiteForm(request.POST)
        if form.is_valid():
            id_menbre = form.cleaned_data['menbre']
            quartier = form.cleaned_data['quartier']

            if Comite.objects.filter(menbre=id_menbre).exists():
                # Le membre existe déjà, ajoutez un message d'erreur
                messages.error(request, 'ce membre existe déjà dans un autre comité.')
                return render(request, 'diacre/ajouter_comite.html',
                              {'form': form, 'messages': messages.get_messages(request)})
            else:
                # Le membre n'existe pas, enregistrez-le
                form = ComiteForm(request.POST, initial={'quartier': quartier_instance})
                form.save()
                messages.success(request, f'Un membre a été ajouté au comité du {quartier.nom}')
                return redirect('gestMenb:Quartier_view')
        else:
            messages.error(request, "Une erreur est survenue lors de l'enregistrement du membre, Veuillez remplir "
                                    "tous les champs ou ce membre existe déjà dans un autre comité.")
            return render(request, 'diacre/ajouter_comite.html',
                          {'form': form, 'messages': messages.get_messages(request)})
    else:
        form = ComiteForm(initial={'quartier': quartier_instance})

    return render(request, "diacre/ajouter_comite.html", context={"form": form})


@login_required(login_url='gestMenb:login_view')
def Modifier_comite(request, cle):
    comite = Comite.objects.get(id=cle)
    nom = comite.quartier.nom
    if request.method == 'POST':
        form = ComiteForm(request.POST, instance=comite)
        if form.is_valid():
            form.save()
            messages.success(request, f'Un membre du comité du {nom} a été modifié!')
            return redirect('gestMenb:Quartier_view')

        else:
            messages.error(request, "Une erreur est survenue lors de la mise à jour.")
            return redirect('gestMenb:Modifier_comite', cle=cle)
    else:
        form = ComiteForm(instance=comite)
        return render(request, 'diacre/modifier_comite.html', context={"form": form})


@login_required(login_url='gestMenb:login_view')
def Supprimer_Menbre_comite(request, cle):
    comite = Comite.objects.get(id=cle)
    nom = comite.quartier.nom
    comite.delete()
    messages.success(request, f'Un membre du comité du {nom} a été supprimé!')
    return redirect('gestMenb:Quartier_view')


@login_required(login_url='gestMenb:login_view')
def Evenements(request):
    events = Evenement.objects.all().order_by('-id')
    evenement_filter = EvenementFilter(request.GET, queryset=events)
    filtered_menbres = evenement_filter.qs
    nombre = filtered_menbres.count()
    if request.method == 'POST':
        form = EvenementForm(request.POST)
        if form.is_valid():
            evenement = form.save(commit=False)
            evenement.save()
            form.save_m2m()  # Enregistrer les membres associés
            messages.success(request, "Un événement a été ajouter avec succès ")
            return redirect('gestMenb:Evenement')
        else:
            messages.error(request, "Une erreur est survenue lors de l'ajout de l'événement.")
            return redirect('gestMenb:Evenement')
    else:
        form = EvenementForm()
    return render(request, "diacre/Evenement.html",
                  context={"Events": filtered_menbres, "evenement_filter": evenement_filter, "nombre": nombre,
                           "form": form})


@login_required(login_url='gestMenb:login_view')
def Detail_Evenements(request, cle):
    events = Evenement.objects.get(id=cle)
    membres_selectionnes = events.membres.all().values_list('id', flat=True)
    today = now().date()
    event_date = events.date_even
    if event_date:
        if event_date < today:
            event_passe = "Passé"
        else:

            time_remaining = event_date - today
            event_passe = f"{time_remaining.days} jours restants"

    event_id = Evenement.objects.get(id=cle)
    if request.method == 'POST':
        form = EvenementForm(request.POST, instance=event_id)
        if form.is_valid():
            form.save()
            messages.success(request, "Evénement mis à jour avec succès")
            return redirect('gestMenb:Evenement')

        else:
            messages.error(request, "Une erreur est survenue lors de la mise à jour.")
            return redirect('gestMenb:Detail_Evenements', cle=cle)
    else:
        form = EvenementForm(instance=event_id)

    return render(request, "diacre/detail_Evenement.html",
                  context={"events": events, "event_passe": event_passe, "form": form,
                           "membres_selectionnes": membres_selectionnes})


@login_required(login_url='gestMenb:login_view')
@csrf_exempt
def delete_event(request, cle):
    try:
        event = Evenement.objects.get(id=cle)
        event.delete()
        return JsonResponse({'status': 'success'})
    except Evenement.DoesNotExist:
        return JsonResponse({'status': 'fail', 'message': 'Item not found'}, status=404)


@login_required(login_url='gestMenb:login_view')
def culte(request):
    return render(request, "diacre/culte.html")


@login_required(login_url='gestMenb:login_view')
def culte_create(request):
    if request.method == 'POST':
        form = CulteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Un culte à été ajouté avec succès")
            return redirect('gestMenb:culte_consultation')
    else:
        initial_data = {'date': date.today()}
        form = CulteForm(initial=initial_data)

    return render(request, 'diacre/demarrer_culte.html', {'form': form})


@login_required(login_url='gestMenb:login_view')
def culte_consultation(request):
    list_cultes = Culte.objects.order_by('-id')
    myFilter = CulteFilter(request.GET, queryset=list_cultes)
    filtered_cultes = myFilter.qs
    nombre = filtered_cultes.count()
    paginator = Paginator(filtered_cultes, 10)  # Paginer les objets avec 10 objets par page
    page = request.GET.get('page')
    objets_page = paginator.get_page(page)
    date_actuelle = date.today()

    return render(request, 'diacre/consulter_culte.html', context={"objets_page": objets_page,
                                                                   "nombre": nombre,
                                                                   "myFilter": myFilter,
                                                                   "date_actuelle": date_actuelle})


@login_required(login_url='gestMenb:login_view')
def vue_culte(request, cle):
    culte = Culte.objects.get(id=cle)
    date_actuelle = date.today()
    date_culte = culte.date
    heure_d = culte.heure_debut
    heure_f = culte.heure_fin
    effectif = culte.nombre_membres
    communiquer = culte.communication
    temoinage = culte.temoignages_du_jour
    cantiques = culte.cantiques_speciaux
    anniversaire = culte.anniversaire
    consecration = culte.consecration
    remerciement = culte.remerciement
    predicateur = culte.predicateur
    if predicateur:
        predic = predicateur
    else:
        predic = culte.predicateur_visiteur

    return render(request, 'diacre/vue_culte.html',
                  context={"date_culte": date_culte, "predicateur": predic, "heure_d": heure_d, "heure_f": heure_f,
                           "effectif": effectif, "communiquer": communiquer, "temoinage": temoinage,
                           "cantiques": cantiques, "anniversaire": anniversaire, "consecration": consecration,
                           "remerciement": remerciement, "date_actuelle": date_actuelle, "cle": cle})


@login_required(login_url='gestMenb:login_view')
def Modifier_culte(request, cle):
    culte = Culte.objects.get(id=cle)
    date = culte.date
    diacres_selectionnes = culte.diacres.all().values_list('id', flat=True)
    if request.method == 'POST':
        form = CulteForm(request.POST, instance=culte)
        if form.is_valid():
            form.save()
            messages.success(request, f'Le culte du {date} a été modifié!')
            return redirect('gestMenb:culte_consultation')

        else:
            messages.error(request, "Une erreur est survenue lors de la mise à jour.")
            return redirect('gestMenb:Modifier_culte', cle=cle)
    else:
        form = CulteForm(instance=culte)
        return render(request, 'diacre/modifier_culte.html',
                      context={"form": form, "diacres_selectionnes": diacres_selectionnes})


@login_required(login_url='gestMenb:login_view')
@csrf_exempt
def delete_culte(request, cle):
    try:
        culte = Culte.objects.get(id=cle)
        culte.delete()
        return JsonResponse({'status': 'success'})
    except Culte.DoesNotExist:
        return JsonResponse({'status': 'fail', 'message': 'Item not found'}, status=404)
