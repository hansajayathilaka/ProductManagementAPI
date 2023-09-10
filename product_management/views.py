from rest_framework import generics, permissions

from product_management import serializers
from product_management.models import Product


class ProductManagementView(generics.ListCreateAPIView):
    serializer_class = serializers.ProductManagementSerializer
    queryset = Product.objects.all()
    permission_classes = (permissions.AllowAny,)


class ProductManagementDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProductManagementSerializer
    queryset = Product.objects.all()
    permission_classes = (permissions.AllowAny,)
