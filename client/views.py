from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializer import MijozSerizalizer
from .models import Mijoz

class MijozListCreateApiView(ListCreateAPIView):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerizalizer

