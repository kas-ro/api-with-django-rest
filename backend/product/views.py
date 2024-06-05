from django.http import JsonResponse
from django.shortcuts import render
from django.forms.models import model_to_dict

from product.models import Product
from .serializer import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

class DetailProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProductView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DeleteProductView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# @api_view(['GET', 'POST'])
# def api_product_view(request):
    # query = Product.objects.all().order_by('?').first()
    # data = {}
    # data = ProductSerializer(data=request.data)
    # if data.is_valid():
    #    instance = data.save()
    #    return Response(data.data)
    # else:
    #     return Response({"detail": "invalid data"})
    # if query:
    #     # data = model_to_dict(query)
    #     data = ProductSerializer(query).data
    # print(data)

    # return JsonResponse(data)
