from rest_framework import generics
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer, ProductStockUpdateSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return ProductStockUpdateSerializer
        return ProductSerializer

    def update(self, request, *args, **kwargs):
        partial = 'partial' in request.data
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
