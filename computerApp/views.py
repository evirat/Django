from django.shortcuts import render, get_object_or_404, redirect 
from computerApp.models import Machine
from .forms import AddMachineForm

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