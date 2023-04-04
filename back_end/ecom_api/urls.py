from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.getProducts, name='products'),
    path('products/<str:pk>/', views.getProduct, name='product'),
    path('products/<str:pk>/reviews/', views.createProductReview, name='create-review'),
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register/', views.registerUser, name='register'),
    path('users/profile/', views.getUserProfile, name='users-profile'),
    path('users/profile/update/', views.updateUserProfile, name='user-profile-update'),
    path('orders/', views.getOrders, name='orders'),
    path('orders/add/', views.addOrderItems, name='order-add'),
    path('orders/<str:pk>/pay/', views.updateOrderToPaid, name='pay'),
    path('orders/<str:pk>/deliver/', views.updateOrderToDelivered, name='deliver'),
    path('orders/<str:pk>/', views.getOrderById, name='user-order'),
    path('orders/<str:pk>/items/', views.getOrderItems, name='order-items'),
    path('orders/myorders/', views.getMyOrders, name='myorders'),
    path('users/', views.getUsers, name='users'),
    path('users/<str:pk>/', views.getUserById, name='user'),
    path('users/<str:pk>/update/', views.updateUser, name='user-update'),
    path('users/<str:pk>/delete/', views.deleteUser, name='user-delete'),
]
