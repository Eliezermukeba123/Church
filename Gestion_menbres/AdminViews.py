from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.utils import timezone

from .filters import CulteFilter
from .forms import CulteForm
from .models import Menbres, Evenement, Culte


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
def Admin_view(request):
    culte = None
    offrande = None
    offrande_const = None

    try:
        membres = Menbres.objects.all().count()
        culte = Culte.objects.latest('id')
        offrande = culte.nombre_offrandes
        offrande_const = culte.nombre_construction

    except Culte.DoesNotExist:

        # Handle the case where the object does not exist
        print("Culte with this ID does not exist.")

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

    return render(request, "administrateur/dashboard.html", context={"membres": membres, "events": events,
                                                                     "pourcentage_homme": pourcentage_homme,
                                                                     "pourcentage_femme": pourcentage_femme,
                                                                     "January": January,
                                                                     "February": February, "March": March,
                                                                     "April": April,
                                                                     "May": May, "June": June, "July": July,
                                                                     "August": August,
                                                                     "September": September, "October": October,
                                                                     "November": November, "December": December,
                                                                     "offrande": offrande, "offrande_const": offrande_const})


@login_required(login_url='gestMenb:login_view')
def culte_consultation_admin(request):
    list_cultes = Culte.objects.order_by('-id')
    myFilter = CulteFilter(request.GET, queryset=list_cultes)
    filtered_cultes = myFilter.qs
    nombre = filtered_cultes.count()
    paginator = Paginator(filtered_cultes, 10)  # Paginer les objets avec 10 objets par page
    page = request.GET.get('page')
    objets_page = paginator.get_page(page)
    date_actuelle = date.today()

    return render(request, 'administrateur/culteAdmin.html', context={"objets_page": objets_page,
                                                                      "nombre": nombre,
                                                                      "myFilter": myFilter,
                                                                      "date_actuelle": date_actuelle})


@login_required(login_url='gestMenb:login_view')
def vue_culte_admin(request, cle):
    culte = Culte.objects.get(id=cle)
    date_actuelle = date.today()
    date_culte = culte.date
    heure_d = culte.heure_debut
    heure_f = culte.heure_fin
    off_regulier = culte.nombre_offrandes
    off_construction = culte.nombre_construction

    return render(request, 'administrateur/vue_culte.html',
                  context={"date_culte": date_culte, "heure_d": heure_d, "heure_f": heure_f,
                           "date_actuelle": date_actuelle, "cle": cle, "off_regulier": off_regulier,
                           "off_construction": off_construction})


@login_required(login_url='gestMenb:login_view')
def Modifier_culte_admin(request, cle):
    culte = Culte.objects.get(id=cle)
    date = culte.date

    if request.method == 'POST':
        form = CulteForm(request.POST, instance=culte)
        if form.is_valid():
            nombre_offrandes_value = form.cleaned_data.get('nombre_offrandes', form.instance.nombre_offrandes)
            nombre_construction_value = form.cleaned_data.get('nombre_construction', form.instance.nombre_construction)

            # Assign the extracted values to the instance
            form.instance.nombre_offrande = nombre_offrandes_value
            form.instance.nombre_construction = nombre_construction_value

            # Save the form
            form.save()

            messages.success(request, f'Le culte du {date} a été modifié!')
            return redirect('gestMenb:culte_consultation_admin')

        else:
            print(form.errors)
            messages.error(request, "Une erreur est survenue lors de la mise à jour.")
            return redirect('gestMenb:Modifier_culte_admin', cle=cle)
    else:
        form = CulteForm(instance=culte)
        return render(request, 'administrateur/modifier_culte.html',
                      context={"form": form})
