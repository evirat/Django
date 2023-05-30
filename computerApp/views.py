from django.shortcuts import render, get_object_or_404, redirect 
from computerApp.models import Machine, Personne
from .forms import AddMachineForm, AddPersonneForm, InfrastructureForm
from django.contrib.auth import authenticate, login
from .models import Infrastructure

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