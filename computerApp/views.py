from django.shortcuts import render, get_object_or_404, redirect 
from computerApp.models import Machine, Personne, Commutateur
from .forms import AddMachineForm, AddPersonneForm, InfrastructureForm, AddCommutateurForm, MaintenanceForm
from django.contrib.auth import authenticate, login
from .models import Infrastructure, Maintenance
from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.mail import send_mail

# Create your views here.
def index(request):
    machines = Machine.objects.all()
    context = {}
    return render(request, 'index.html', context)

def machine_list_view(request):
    machines = Machine.objects.all()
    context = {'machines':machines}
    return render(request, 'computerApp/machine_list.html', context)

def machine_detail_views(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    context = {'machine': machine}
    return render(request, 'computerApp/machine_detail.html', context)

def machine_add_form(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            new_machine = Machine(nom=form.cleaned_data['nom'])
            new_machine.save()
            return redirect('machines')

    else:
        form = AddMachineForm()
        context = {'form' : form}
        return render(request, 'computerApp/machine_add.html', context)

def machine_delete_views(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    if request.method == 'POST':
        machine.delete()
        return redirect('machines')
    context = {'machine': machine}
    return render(request, 'computerApp/machine_delete.html', context)

def personne_list_view(request):
    personnes = Personne.objects.all()
    context = {'personnes':personnes}
    return render(request, 'computerApp/personne_list.html', context)

def personne_detail_views(request, pk):
    personne = get_object_or_404(Personne, id=pk)
    context = {'personne': personne}
    return render(request, 'computerApp/personne_detail.html', context)

def personne_add_form(request):
    if request.method == 'POST':
        form = AddPersonneForm(request.POST or None)
        if form.is_valid():
            new_personne = Personne(nom=form.cleaned_data['nom'])
            new_personne.save()
            return redirect('personnes')

    else:
        form = AddPersonneForm()
        context = {'form' : form}
        return render(request, 'computerApp/personne_add.html', context)

def personne_delete_views(request, pk):
    personne = get_object_or_404(Personne, id=pk)
    if request.method == 'POST':
        personne.delete()
        return redirect('personnes')
    context = {'personne': personne}
    return render(request, 'computerApp/personne_delete.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index.html')  # Redirige vers la page d'accueil après la connexion
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
            return render(request, 'computerApp/login.html', {'error_message': error_message})
    else:
        return render(request, 'templates/computerApp/login.html')

def infrastructures(request):
    infrastructures = Infrastructure.objects.all()
    context = {'infrastructures': infrastructures}
    return render(request, 'computerApp/infrastructures.html', context)

def add_infrastructure(request):
    if request.method == 'POST':
        form = InfrastructureForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            machines = form.cleaned_data['machines']
            infrastructure = Infrastructure.objects.create(nom=nom)
            infrastructure.machines.set(machines)
            return redirect('infrastructures')
    else:
        form = InfrastructureForm()
    return render(request, 'computerApp/infra_add.html', {'form': form})

def delete_infrastructure(request, infrastructure_id):
    infrastructure = Infrastructure.objects.get(pk=infrastructure_id)
    infrastructure.delete()
    return redirect('infrastructures')

def infrastructure_details(request, infrastructure_id):
    infrastructure = Infrastructure.objects.get(pk=infrastructure_id)
    machines = infrastructure.machines.all()
    context = {
        'infrastructure': infrastructure,
        'machines': machines
    }
    return render(request, 'computerApp/infrastructure_details.html', context)

#Pour les commutateurs

def commu_list_view(request):
    coms = Commutateur.objects.all()
    context = {'coms':coms}
    return render(request, 'computerApp/commu_list.html', context)

def commu_detail_views(request, pk):
    com = get_object_or_404(Commutateur, id=pk)
    context = {'com': com}
    return render(request, 'computerApp/commu_detail.html', context)

def commu_add_form(request):
    if request.method == 'POST':
        form = AddCommutateurForm(request.POST or None)
        if form.is_valid():
            new_commu = Commutateur(nom=form.cleaned_data['nom'])
            new_commu.save()
            return redirect('coms')

    else:
        form = AddCommutateurForm()
        context = {'form' : form}
        return render(request, 'computerApp/commu_add.html', context)

def commu_delete_views(request, pk):
    com = get_object_or_404(Commutateur, id=pk)
    if request.method == 'POST':
        com.delete()
        return redirect('coms')
    context = {'com': com }
    return render(request, 'computerApp/commu_delete.html', context)

#Vue pour afficher la liste des entretiens et des maintenances préventives :

def maintenance_list_views(request):
    maintenances = Maintenance.objects.all()
    context = {'maintenances': maintenances}
    return render(request, 'computerApp/maintenance_list.html', context)


#Vue pour créer un nouvel entretien ou une nouvelle maintenance préventive

def create_maintenance_views(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maintenances')
    else:
        form = MaintenanceForm()
    return render(request, 'computerApp/create_maintenance.html', {'form': form})