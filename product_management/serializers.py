from rest_framework import serializers

from product_management.models import Product


class ProductManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity')
        read_only_fields = ('id',)


class ProductManagementOrderSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    quantity = serializers.FloatField()

    class Meta:
        model = Product
        fields = ('product_id', 'quantity')
