from django.shortcuts import render
from btc.models import Price, MockPrice, MockFuturePrice
from django.http import HttpResponse
from rest_framework import viewsets
from btc.serializers import PriceSerializer, MockPriceSerializer, MockFuturePriceSerializer
from itertools import chain
# Create your views here.


class PriceViewSet(viewsets.ModelViewSet):
    queryset = MockPrice.objects.all()
    serializer_class = MockPriceSerializer

class FuturePriceViewSet(viewsets.ModelViewSet):
    queryset = MockFuturePrice.objects.all()
    serializer_class = MockFuturePriceSerializer
