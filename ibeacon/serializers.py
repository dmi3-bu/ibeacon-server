from rest_framework import serializers
from .models import Beacon


class BeaconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beacon
        fields = ('id', 'title', 'UUID', 'description')
