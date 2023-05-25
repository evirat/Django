from django import forms
from django.core.exceptions import ValidationError

class AddMachineForm(forms.Form) : 
    nom = forms.CharField(required = True, label= 'Nom de la machine')
    prenom = forms.CharField(required = True, label= 'Propriétaire')
    type = forms.CharField(required = True, label= 'Type de la machine')

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