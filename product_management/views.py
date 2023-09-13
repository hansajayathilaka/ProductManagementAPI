from rest_framework import generics, permissions, status
from rest_framework.response import Response

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


class ProductManagementOrderView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.ProductManagementOrderSerializer

    def patch(self, request, *args, **kwargs):
        errors = []
        for data in request.data:
            _data = dict(data)
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                obj = Product.objects.get(id=data.get('product_id'))
                quantity = obj.quantity - data.get('quantity')
                serializer.update(instance=obj, validated_data={'quantity': quantity})
            else:
                errors.append(serializer.errors)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)
