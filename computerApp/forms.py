from django import forms
from django.core.exceptions import ValidationError
from computerApp.models import Machine, Personne, Maintenance
from django.db import models

class AddMachineForm(forms.Form) : 

    nom = forms.CharField(required = True, label= 'Nom de la machine')
    type_machine = forms.ChoiceField(choices=Machine.TYPE, label='Type de machine')
    description = forms.CharField(required = True, label= 'Nom du propriétaire')

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 6:
            raise ValidationError(("Erreur de format pour le champ nom"))

        return data

class AddPersonneForm(forms.Form) : 
    nom = forms.CharField(required = True, label= 'Nom ')
    prenom = forms.CharField(required = True, label= 'Prenom')

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 6:
            raise ValidationError(("Erreur de format pour le champ nom"))

        return data       

class InfrastructureForm(forms.Form):
    nom = forms.CharField(required=True, label='Nom de l\'infrastructure')
    machines = forms.ModelMultipleChoiceField(queryset=Machine.objects.all(), widget=forms.CheckboxSelectMultiple)

class AddCommutateurForm(forms.Form) : 

    nom = forms.CharField(required = True, label= 'Nom ')
    prenom = forms.CharField(required = True, label= 'Prenom')

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 6:
            raise ValidationError(("Erreur de format pour le champ nom"))

        return data 


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ('machine', 'date', 'description')