from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import ProductSerializer
from .models import Product

class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all().order_by('name')
  serializer_class = ProductSerializer
  lookup_field = 'barcode'
  
  @action(detail=False)
  def search(self, request):
    query = self.request.query_params.get('query')
    values = Product.objects.filter(Q(name__icontains=query) | Q(barcode__icontains=query)).values()
    return Response(values)

  @action(detail=False)
  def order(self, request):
    order_by = request.query_params.get('property')
    values = Product.objects.all().order_by(order_by).values()
    order = request.query_params.get('order')
    if (order == "desc"):
      values = values.reverse()
    return Response(values)
