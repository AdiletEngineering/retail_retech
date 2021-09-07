from rest_framework import serializers

from .models import *

class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class StoreDetailSerializer(serializers.ModelSerializer):
    supplies = SupplySerializer(many=True)
    class Meta:
        model = Store
        fields = '__all__'
