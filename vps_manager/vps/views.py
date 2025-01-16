from rest_framework.viewsets import ModelViewSet
from vps.models import VPS
from vps.serializers import VPSSerializer


class VPSViewSet(ModelViewSet):
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer
