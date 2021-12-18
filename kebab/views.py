from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import  DjangoModelPermissions
from rest_framework import viewsets
from .models import *
from rest_framework.decorators import api_view, schema
import json
from django.http import JsonResponse

@api_view(['GET'])
def get_menu(request):
    menus = Menyu.objects.all()
    datas = list(menus.values())
    for data in datas:
        category = Category.objects.get(id=data["category_id"])
        data["category_id"] = category.name
    return JsonResponse(datas, safe=False)
    
@api_view(['GET'])
def get_menu(request):
    menul = Special.objects.all()
    datas = list(menul.values())
    for data in datas:
        category = Category_1.objects.get(id=data["category_id"])
        data["category_id"] = category.name
    return JsonResponse(datas, safe=False)
    
class MenyuViewSet(viewsets.ModelViewSet):
    queryset = Menyu.objects.all()
    serializer_class = MenyuSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [ DjangoModelPermissions]
    filter_backends = [filters.OrderingFilter,DjangoFilterBackend,filters.SearchFilter]
    ordering_fields = ['name','price']
    ordering = ['id']
    search_fields = ['name']
    filterset_fields = ['name',]



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SpecialViewSet(viewsets.ModelViewSet):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [ DjangoModelPermissions]
    filter_backends = [filters.OrderingFilter,DjangoFilterBackend,filters.SearchFilter]
    ordering_fields = ['name','price']
    ordering = ['id']
    search_fields = ['^name']
    filterset_fields = ['name',]


class Category_1ViewSet(viewsets.ModelViewSet):
    queryset = Category_1.objects.all()
    serializer_class = Category_1Serializer


class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class ChefViewSet(viewsets.ModelViewSet):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer




class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [ DjangoModelPermissions]
    filter_backends = [filters.OrderingFilter,DjangoFilterBackend,filters.SearchFilter]
    ordering_fields = ['name','subject']
    ordering = ['subject']
    search_fields = ['name']
    filterset_fields = ['name',]

class CardItemViewSet(viewsets.ModelViewSet):
    queryset = CardItem.objects.all()
    serializer_class = CardItemSerializer        

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer