from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('customer/<int:customer_id>/orders/', views.customer_orders, name='customer_orders'),
    path('search/', views.search_customers, name='search_customers'),
    path('orders/', views.filter_orders, name='filter_orders'),
    path('sales-total/', views.total_sales, name='total_sales'),
    path('top-products/', views.top_products, name='top_products'),
    path('customer-order-count/', views.customer_order_count, name='customer_order_count'),
]


