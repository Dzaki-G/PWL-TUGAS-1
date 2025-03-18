from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.view_products, name='view_products'),
    path('product/<int:id>/', views.view_product, name='view_product'),
]
