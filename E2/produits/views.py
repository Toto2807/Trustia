from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Produit, Facture
from .forms import ProduitForm, FactureItemFormSet


def liste_produits(request):
    produits = Produit.objects.all()
    paginator = Paginator(produits, 5)
    page = request.GET.get('page')
    produits_page = paginator.get_page(page)
    return render(request, 'produits/liste_produits.html', {'produits': produits_page})

def creer_produit(request):
    form = ProduitForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_produits')
    return render(request, 'produits/form_produit.html', {'form': form, 'titre': 'Créer un produit'})

def modifier_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    form = ProduitForm(request.POST or None, instance=produit)
    if form.is_valid():
        form.save()
        return redirect('liste_produits')
    return render(request, 'produits/form_produit.html', {'form': form, 'titre': 'Modifier un produit'})

def supprimer_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('liste_produits')
    return render(request, 'produits/confirmer_suppression.html', {'produit': produit})



def liste_factures(request):
    factures = Facture.objects.all()
    paginator = Paginator(factures, 5)
    page = request.GET.get('page')
    factures_page = paginator.get_page(page)
    return render(request, 'produits/liste_factures.html', {'factures': factures_page})

def creer_facture(request):
    facture = Facture()
    if request.method == 'POST':
        formset = FactureItemFormSet(request.POST, instance=facture)
        if formset.is_valid():
            facture.save()
            formset.save()
            return redirect('detail_facture', pk=facture.pk)
    else:
        formset = FactureItemFormSet(instance=facture)
    return render(request, 'produits/form_facture.html', {'formset': formset})

def detail_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    return render(request, 'produits/detail_facture.html', {'facture': facture})