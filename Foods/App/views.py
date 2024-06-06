from django.shortcuts import render
from rest_framework import viewsets
from .models import Food,FoodType,Comment
from rest_framework import permissions
from .serializers import FoodSerializers, FoodTypeSerializers, CommentSerializers
from rest_framework.authentication import TokenAuthentication
# Create your views here.
class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [permissions.DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]

class FoodTypeViewSet(viewsets.ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializers
    permission_classes = [permissions.DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [permissions.DjangoModelPermissions]

