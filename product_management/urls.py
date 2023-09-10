from django.urls import path

from product_management.views import ProductManagementView, ProductManagementDetailView


urlpatterns = [
    path('', ProductManagementView.as_view(), name='product_management'),
    path('<int:pk>/', ProductManagementDetailView.as_view(), name='product_management_detail'),
]
