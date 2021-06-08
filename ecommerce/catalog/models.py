from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    price = models.FloatField()
    # il prezzo originale - per applicare gli sconti
    compare_to = models.FloatField()
    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    # last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # quantità di tutte le varianti
    @property
    def quantity(self):
        variants = Variant.objects.filter(product=self)
        if variants.count() <= 0: return 0
        return sum(x.quantity for x in variants) 

    @property 
    def available_sizes(self):
        variants = Variant.objects.filter(product=self)




class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku = models.CharField(unique=True, max_length=200)
    quantity = models.IntegerField(default=0)

    class Size(models.TextChoices):
        SMALL = 'S', _('Small')
        MEDIUM = 'M', _('Medium')
        LARGE = 'L', _('Large')
        EXTRA_LARGE = 'XL', _('Extra-Large')

    size = models.CharField(max_length=2, choices=Size.choices, default=Size.SMALL)

    def __str__(self):
        return '{}-{}'.format(self.product.name, self.size)



class Category(models.Model):
    name = models.CharField(max_length=200)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.name

