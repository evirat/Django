from django.shortcuts import render, get_object_or_404, redirect 
from computerApp.models import Machine
from .forms import AddMachineForm
from django.contrib.auth import authenticate, login

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

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirection vers la page index.html
        else:
            # Gérer les erreurs d'authentification incorrecte
            pass
    return render(request, 'login.html')   