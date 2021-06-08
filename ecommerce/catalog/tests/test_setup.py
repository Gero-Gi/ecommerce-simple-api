from django.test import client
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from catalog import models
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
USER = get_user_model()




class APITestMixin():
    def get_admin_user(self):
        admin = USER.objects.create(
            first_name='admin',
            last_name='admin',
            email='admin@admin.com',
            is_superuser=True,
        )
        admin.set_password('adminpass')
        admin.save()
        return admin

    def get_user():
        user = USER.objects.create(
            first_name='John',
            last_name='Doe',
            email='john@gmail.com',
            is_superuser=False,
        )
        user.set_password('password')
        user.save()
        return user


    def token_authentication(self, user):
        token, created = Token.objects.get_or_create(user=user)

        self.client = APIClient()
        self.client.force_authenticate(user=user, token=token)
        self.authorization = 'Token {}'.format(token.key)
        self.client.credentials = {'Authorization': self.authorization}



    




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

    def get_admin(self):
        admin = USER.objects.create(
            first_name='admin',
            last_name='admin',
            email='admin@admin.com',
            is_superuser=True,
        )
        admin.set_password('adminpass')
        admin.save()
        return admin


class ProductTestSetup(CatalogTestMixin, APITestMixin, APITestCase):

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

        self.token_authentication(self.get_admin_user())
        



class VariantTestSetup(CatalogTestMixin, APITestMixin, APITestCase):

    def setUp(self):
        self.url = reverse('variant-list')

        self.test_product = self.get_test_product()

        self.json_patch_data = {
            'quantity': 100,
        }

        self.token_authentication(self.get_admin_user())


class CategoryTestSetUp(CatalogTestMixin, APITestMixin, APITestCase):

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

        self.token_authentication(self.get_admin_user())


        

