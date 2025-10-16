from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product
from .serializers import ProductSerializer
from.permessions import IsOwnerOrReadOnly


# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
  
    # a view with pre made list , create , retrieve , update , delete.
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):

        # Overriding the method to make the logged in user the owner when he creates a product.

        serializer.save(owner=self.request.user)