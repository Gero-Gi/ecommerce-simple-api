from django.test import client
from rest_framework.test import APITestCase, APIClient
from rest_framework.routers import reverse
from catalog import models as catalog
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
USER = get_user_model()



class AuthTestMixin():
    def get_user(self, first_name, is_superuser=False):
        user = USER.objects.create(
            first_name=first_name,
            is_superuser=is_superuser,
            last_name = 'last_name',
            email = '{}@gmail.com'.format(first_name)
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

    def get_product(self, name):
        product = catalog.Product.objects.create(
            name=name,
            description='description',
            price = 10,
            compare_to = 10,
            )
        variants = catalog.Variant.objects.filter(product=product)
        for variant in variants:
            variant.quantity = 5
            variant.save()
        return product
        
   
class OrderProcessSetUp(AuthTestMixin, CatalogTestMixin, APITestCase):
    
 
    def setUp(self):
        self.auth_user = self.get_user('main')
        self.item_url = reverse('item-list')
        self.address_url = reverse('address-list')
        self.order_url = reverse('order-list')
        self.token_authentication(self.auth_user)

        self.products = []
        for i in range(0,2):
            self.products.append(self.get_product('product{}'.format(i)))









