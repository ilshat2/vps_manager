from rest_framework import serializers
from vps.models import VPS


class VPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = VPS
        fields = '__all__'
