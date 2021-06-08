from . import test_setup
from catalog import models



class ProductTest(test_setup.ProductTestSetup):

    def test_creation(self):
        res = self.client.post(self.url, self.json_post_data, headers={'Authorization':self.authorization})
        # print('POST\n{}\n'.format(res.data))
        self.assertEqual(res.status_code, 201)
        # testa il numero di varianti create
        self.assertEqual(len(res.data['variants']), 4)

    def test_update(self):
        self.url = '{}{}/'.format(self.url, self.test_product.id)
        res = self.client.patch(self.url, self.json_patch_data, format='json', headers={'Authorization':self.authorization})
        # print('PATCH\n{}\n'.format(res.data))

        self.assertEqual(res.data['name'], 'product_updated' )
        product = models.Product.objects.get(id=res.data['id'])
        self.assertEqual(product.name, 'product_updated')

class VariantTest(test_setup.VariantTestSetup):
  
    def test_update(self):
        variants = models.Variant.objects.filter(product=self.test_product)
        for v in variants:
            url = '{}{}/'.format(self.url, v.id)
            res = self.client.patch(url, self.json_patch_data, format='json', headers={'Authorization':self.authorization})
            # print('PATCH-variant_{}\n{}\n'.format(v.id, res.data))
            self.assertEqual(res.data['quantity'], 100)
        self.assertEqual(models.Product.objects.get(id=self.test_product.id).quantity, 400)

class CategoryTest(test_setup.CategoryTestSetUp):
    
    def test_category(self):
        res = self.client.post(self.url, self.json_post_data, headers={'Authorization':self.authorization})
        self.assertEqual(res.status_code, 201)
        # print('POST-category\n{}\n'.format(res.data))

        url_category = '{}{}/'.format(self.url, res.data['id'])

        patch_data = {
            'products':[]
        }

        for i in range(0,4):
            product = self.get_test_product(name='product{}'.format(i))
            patch_data['products'].append(product.id)


        res = self.client.patch(url_category, patch_data, format='json', headers={'Authorization':self.authorization})
        # print('PATCH-category\n{}\n'.format(res.data))
        self.assertEqual(res.status_code, 200)

        patch_data = {
            'products':[1,2,3]
        }

        res = self.client.patch(url_category, patch_data, format='json', headers={'Authorization':self.authorization})
        # print('PATCH-category\n{}\n'.format(res.data))
        self.assertEqual(len(res.data['products']), 2)
        


        
        

