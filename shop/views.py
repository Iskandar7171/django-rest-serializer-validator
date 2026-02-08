from rest_framework.generics import ListCreateAPIView
from .serializer import CategorySerializer,ProductSerializer
from .models import Category,Product

class CategoryListCreateApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class ProductListCreateApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer