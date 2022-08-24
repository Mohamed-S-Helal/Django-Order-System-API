from django.urls import path
from . import views


urlpatterns = [
    path('get_products/', views.ListProductAPIView.as_view()),
    path('create_product/', views.CreateProductAPIView.as_view()),
    path('modify_product/<int:pk>/', views.UpdateProductAPIView.as_view()),
    path('delete_product/<int:pk>/', views.DestroyProductAPIView.as_view()),
    path('purchase_product/<int:pk>/', views.PurchaseCreateView.as_view()),
    path('get_purchased/', views.ListPurchaseProductAPIView.as_view()),
]