from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    quantity = models.FloatField()

    class meta:
        app_label = 'product_management'
