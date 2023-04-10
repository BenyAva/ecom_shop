from django.urls import path
from ecom_api.views import product_views as views

urlpatterns = [
    path('', views.getProducts, name='products'),
    path('create/', views.createProduct, name='product-create'),
    path('upload/', views.uploadImage, name='image-upload'),
    path('<str:pk>/', views.getProduct, name='product'),
    path('<str:pk>/update/', views.updateProduct, name='product-update'),
    path('<str:pk>/delete/', views.deleteProduct, name='product-delete'),
]