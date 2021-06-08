from django.db import models
from django.contrib.auth import get_user_model
USER = get_user_model()
from catalog.models import Variant


class Cart(models.Model):
    user = models.OneToOneField(USER, on_delete=models.CASCADE)

    def __str__(self):
        return '{}-cart'.format(self.user)

    @property
    def price(self):
        return sum(x.price for x in Item.objects.filter(cart=self))



class Item(models.Model):
    variant = models.ForeignKey(
        'catalog.Variant', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    # True se l'item è nel carrello
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}-cart{}'.format(self.variant, self.cart.id)

    @property
    def price(self):
        return self.quantity * self.variant.product.price


class Address(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    CAP = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    user = models.ForeignKey(USER, on_delete=models.CASCADE)

    def __str__(self):
        return '{}-add{}'.format(self.user, self.id)


class Order(models.Model):
    items = models.ManyToManyField(Item, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    is_shipped = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return 'order-{}'.format(self.id)
