from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Subquery
from .models import Product, Purchase
from .permissions import IsNotCreator
from .serializers import ProductSerializer, PurchaseSerializer
from .pagination import CustomPagination


class ListProductAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated, IsAdminUser]
    

class CreateProductAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def perform_create(self, serializer):
        # Assign the user who created the product
        serializer.save(creator=self.request.user)


class UpdateProductAPIView(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class DestroyProductAPIView(DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class PurchaseCreateView(CreateAPIView):
    serializer_class = PurchaseSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsNotCreator]
    
    
    def perform_create(self, serializer):
        # Assign user and product to purchase
        print(self.kwargs.get('pk'))
        product = get_object_or_404(Product, id=self.kwargs.get('pk'))
        serializer.save(user=self.request.user, product=product)


class ListPurchaseProductAPIView(ListAPIView):
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        purchases = self.request.user.purchase_set
        queryset = Product.objects.filter(purchase__in=Subquery(purchases.values("id")))
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


