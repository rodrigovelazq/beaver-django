from django.shortcuts import render
from rest_framework import viewsets
from .models import Repositories, Owners
from .serializers import OwnersSerializer, RepositoriesSerializer


class RepositoriesView(viewsets.ModelViewSet):
    queryset = Repositories.objects.all()
    serializer_class = RepositoriesSerializer


class OwnersView(viewsets.ModelViewSet):
    queryset = Owners.objects.all()
    serializer_class = OwnersSerializer
