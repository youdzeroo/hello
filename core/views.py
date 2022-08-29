from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from core.models import Cars
from core.serializers import CarsSerializer


class CarsListView(ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
