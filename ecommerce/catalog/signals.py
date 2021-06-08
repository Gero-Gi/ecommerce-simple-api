from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Variant, Product

# genera identificatore, univoco, per le varianti
@receiver(pre_save, sender=Variant)
def generate_sku(sender, instance, **kwargs):
    instance.sku = '{}-{}'.format(instance.product.name, instance.size)

# crea le varianti di un prodotto dopo che questo è stato creato
@receiver(post_save, sender=Product)
def create_variants(sender, instance,**kwargs):
    if Variant.objects.filter(product=instance.id).count() > 0:
        return
    for size in Variant.Size:
        Variant.objects.create(
            product=instance,
            quantity=0,
            size=size,
            sku='{}-{}'.format(instance.name, size),
        )
