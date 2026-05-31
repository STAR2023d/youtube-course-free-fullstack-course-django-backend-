from django.shortcuts import render
from rest_framework.generics import ListAPIView

from products.models import Product, ProductCategory
from products.serializers import ProductCategorySerializer, ProductsSerializer
from products.models import ProductCategory, Maker

from products.serializers import ProductCategorySerializer, MakerSerializer


class ProductCategoryListView(ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()

class MakerListView(ListAPIView):
    serializer_class = MakerSerializer
    queryset = Maker.objects.all()

class ProductsListView(ListAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()    

# Create your views here.
