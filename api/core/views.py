from django.shortcuts import render
from rest_framework import status, viewsets
from .models import *
from .serializer import *
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer