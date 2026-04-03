from django.urls import path
from . import views

urlpatterns = [
    path('',                        views.liste_produits,    name='liste_produits'),
    path('produit/creer/',          views.creer_produit,     name='creer_produit'),
    path('produit/<int:pk>/modifier/', views.modifier_produit, name='modifier_produit'),
    path('produit/<int:pk>/supprimer/', views.supprimer_produit, name='supprimer_produit'),

    path('factures/',               views.liste_factures,    name='liste_factures'),
    path('facture/creer/',          views.creer_facture,     name='creer_facture'),
    path('facture/<int:pk>/',       views.detail_facture,    name='detail_facture'),
]