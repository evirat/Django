from django.shortcuts import render
from computerApp.models import Machine

# Create your views here.
def index(request):
    machines = Machine.objects.all()
    context = {}
    return render(request, 'templates/index.html', context)

def machine_list(request):
    machines = Machine.objects.all()
    context = {'machines':machines}
    return render(request, 'computerApp/machine_list.html', context)