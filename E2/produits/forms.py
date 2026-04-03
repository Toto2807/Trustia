from django import forms
from .models import Produit, Facture, FactureItem

class ProduitForm(forms.ModelForm):
    class Meta:
        model  = Produit
        fields = ['nom', 'prix', 'date_peremption']
        widgets = {
            'date_peremption': forms.DateInput(attrs={'type': 'date'}),
        }


class FactureItemForm(forms.ModelForm):
    class Meta:
        model  = FactureItem
        fields = ['produit', 'quantite']


FactureItemFormSet = forms.inlineformset_factory(
    Facture,
    FactureItem,
    form=FactureItemForm,
    extra=1,
    can_delete=True
)