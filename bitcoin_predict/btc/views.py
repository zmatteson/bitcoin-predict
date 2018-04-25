from django.shortcuts import render
from btc.models import Price, MockPrice
from django.http import HttpResponse
from rest_framework import viewsets
from btc.serializers import PriceSerializer, MockPriceSerializer
from itertools import chain
# Create your views here.


class PriceViewSet(viewsets.ModelViewSet):
    queryset = MockPrice.objects.all()
    serializer_class = MockPriceSerializer
