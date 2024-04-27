from django.db.models import Value
from rest_framework import generics
from rest_framework.response import Response

from . import models
from . import serializers
from .models import Product


class ProductAPI(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class RequestAPI(generics.CreateAPIView):
    serializer_class = serializers.RequestSerializer

    def post(self, request, *args, **kwargs):
        code = request.data['code']
        quantity = request.data['quantity']

        products = Product.objects.filter(code=code).annotate(
            quantity=Value(quantity)
        ).prefetch_related('materials')

        serializer = serializers.ProductResultSerializer(instance=products, many=True)

        return Response({'result': serializer.data})

    def get(self, request):
        return Response({'message': 'GET'})


class ResultAPI(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductResultSerializer

    def get_queryset(self):
        print(self.request.data)
        return super().get_queryset()
