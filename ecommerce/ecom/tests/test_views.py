from django.http import response
from .test_setup import OrderProcessSetUp
from ecom import models
from catalog import models as catalog


class TestOrderProcess(OrderProcessSetUp):

    def test_item(self):
        product = self.get_product('product')
        variant = catalog.Variant.objects.filter(product=product)[0]
        # test creazione
        res = self.client.post(
            self.item_url, data={
                'variant': variant.id,
                'quantity': 1,
                'is_active': True,

            }
        )
        print('POST-Item\n{}\n'.format(res.data))
        
        self.assertEqual(res.status_code, 201)

        url = '{}{}/'.format(self.item_url, res.data['id'])
        res = self.client.get(
            url, 
            format='json'
        )
        print('PATCH-Item\n{}\n'.format(res.data))
        self.assertEqual(res.status_code, 200)


        # test modifica quantità
        res = self.client.patch(
            url, data={
                'quantity': 2000,
            },
            format='json'
        )
        print('PATCH-Item\n{}\n'.format(res.data))
        self.assertEqual(res.status_code, 200)
        