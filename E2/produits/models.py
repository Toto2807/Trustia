from django.db import models

class Produit(models.Model):
    nom             = models.CharField(max_length=200)   
    prix            = models.DecimalField(max_digits=10, decimal_places=2) 
    date_peremption = models.DateField()                

    def __str__(self):
        return self.nom 



class Facture(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)

    def total(self):
        return sum(item.sous_total() for item in self.items.all())

    def nombre_produits(self):
        return sum(item.quantite for item in self.items.all())

    def __str__(self):
        return f"Facture #{self.id}"


class FactureItem(models.Model):
    facture  = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='items')
    produit  = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def sous_total(self):
        return self.produit.prix * self.quantite