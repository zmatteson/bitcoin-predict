from btc.models import Price, MockPrice, MockFuturePrice
from rest_framework import serializers

class PriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Price
        fields = ('price','date')

class MockFuturePriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MockPrice
        fields = ('price','date')

class MockPriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MockPrice
        fields = ('price','date')
