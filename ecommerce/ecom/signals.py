from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from . import models

# setta come inattivi tutti gli items ordinati
# rimuove i prodotti acquistati dall'inventario
@receiver(pre_save, sender=models.Order)
def make_order(sender, instance, **kwargs):
    active_items = models.Item.filter(user=instance.user)
    active_items = active_items.filter(is_active=True)
    for item in active_items:
        instance.items.add(item)
        item.is_active = False
        item.save()
        variant = item.variant
        variant.quantity -= item.quantity
        variant.save()


# rimuove gli items con quantità uguale a zero
@receiver(post_save, sender=models.Item)
def delete_empty_item(sender, instance, **kwargs):
    if instance.quantity <= 0:
        instance.delete()