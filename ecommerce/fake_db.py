from ecom import models as ecom
from catalog import models as catalog
from faker import Faker
import random



class FakeDB():
    _products_per_category = 10
    _categories = ['T-Shirts', 'Pantaloni', 'Giacche']
    _faker = Faker()
    products = []

    def clean_catalog(self):
        catalog.Product.objects.all().delete()
        catalog.Category.objects.all().delete()

    def populate_catalog(self):
        # creazione categorie
        for c in self._categories:
            category = catalog.Category.objects.create(name=c)
            # creazione prodotti
            for i in range(0, self._products_per_category):
                price = round(random.uniform(10, 200), 2)
                compare_to=price
                if random.random() >= 0.5: compare_to = round(price + .3 * price, 2)
                product = catalog.Product.objects.create(
                    name='product-{}{}'.format(category.id, i),
                    description=self._faker.text(max_nb_chars=400, ext_word_list=None),
                    price=price,
                    compare_to=compare_to,
                )
                category.products.add(product)
                category.save()
                self.products.append(product)
                # quantità alle varianti
                for variant in catalog.Variant.objects.filter(product=product):
                    variant.quantity = random.randint(0, 30)
                    variant.save()

  









