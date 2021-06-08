from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from ecom.models import Cart


# crea il carrello collegato a ogni utente
@receiver(post_save, sender=User)
def create_cart(sender, instance, **kwargs):
    try:
        Cart.objects.get(user=instance)
    except:
        Cart.objects.create(user=instance)