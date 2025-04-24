from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop-index'),
    path('product/<slug:slug>/', views.product_detail, name='shop-product-detail'),
]
