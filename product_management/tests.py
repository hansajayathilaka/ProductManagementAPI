from django.test import TestCase
from django.urls import reverse

from product_management.models import Product


class ProductManagementTestCase(TestCase):
    def test_product_management(self):
        self.assertTrue(True)

    def test_product_create(self):
        self.client.post(
            reverse('product_management'),
            {
                'name': 'test product',
                'description': 'test description',
                'price': 1,
                'quantity': 1
            }
        )
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'test product')
        self.assertEqual(Product.objects.get().description, 'test description')
        self.assertEqual(Product.objects.get().price, 1.0)
        self.assertEqual(Product.objects.get().quantity, 1.0)

    def test_product_delete(self):
        self.test_product_create()
        self.client.delete(reverse('product_management_detail', kwargs={'pk': Product.objects.get().id}))
        self.assertEqual(Product.objects.count(), 0)

    def test_product_list(self):
        self.test_product_create()
        self.client.get(reverse('product_management'))
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'test product')
        self.assertEqual(Product.objects.get().description, 'test description')
        self.assertEqual(Product.objects.get().price, 1.0)
        self.assertEqual(Product.objects.get().quantity, 1.0)

    def test_product_detail(self):
        self.test_product_create()
        self.client.get(reverse('product_management_detail', kwargs={'pk': Product.objects.get().id}))
        self.assertEqual(Product.objects.get().name, 'test product')
        self.assertEqual(Product.objects.get().description, 'test description')
        self.assertEqual(Product.objects.get().price, 1.0)
        self.assertEqual(Product.objects.get().quantity, 1.0)

    def test_product_list_filter(self):
        self.test_product_create()
        self.client.get(reverse('product_management') + '?name=test product')
        self.assertEqual(Product.objects.get().name, 'test product')
