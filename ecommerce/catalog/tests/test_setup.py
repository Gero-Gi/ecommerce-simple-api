from rest_framework.test import APITestCase
from django.urls import reverse
from catalog import models


class CatalogTestMixin():
    def get_test_product(self, name='test_product'):
        test_product = models.Product.objects.create(
            name=name,
            description='description',
            price=30,
            compare_to=20,
        )

        category = models.Category.objects.create(name='test_category')
        category.products.add(test_product)
        category.save()

        variants = models.Variant.objects.filter(product=test_product)

        for v in variants:
            v.quantity = 30
            v.save()

        return test_product


class ProductTestSetup(CatalogTestMixin, APITestCase):

    def setUp(self):
        self.url = reverse('product-list')

        self.json_post_data = {
            'name': 'test_product',
            'description': 'test_description',
            'price': 10,
            'compare_to': 5,
        }

        self.test_product = self.get_test_product(name='test_product1')

        self.json_patch_data = {
            'name': 'product_updated',
            'description': 'description_updated',
        }


class VariantTestSetup(CatalogTestMixin, APITestCase):

    def setUp(self):
        self.url = reverse('variant-list')

        self.test_product = self.get_test_product()

        self.json_patch_data = {
            'quantity': 100,
        }


class CategoryTestSetUp(CatalogTestMixin, APITestCase):

    def setUp(self):
        self.url = reverse('category-list')

        
        self.test_product = self.get_test_product()

        self.json_post_data = {
            'name': 'category',
            'products': [1],
        }

        self.json_patch_data = {
            'name': 'category_modified',
            'products': [-self.test_product.id]
        }
