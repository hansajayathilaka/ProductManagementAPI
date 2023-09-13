from django.urls import path

from product_management.views import ProductManagementView, ProductManagementDetailView, ProductManagementOrderView

urlpatterns = [
    path('', ProductManagementView.as_view(), name='product_management'),
    path('<int:pk>/', ProductManagementDetailView.as_view(), name='product_management_detail'),
    path('order', ProductManagementOrderView.as_view(), name='product_management_order'),
]
