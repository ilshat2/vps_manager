from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from vps.models import VPS
from vps.serializers import VPSSerializer


class VPSViewSet(ModelViewSet):
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['status', 'cpu', 'ram', 'hdd']

    @action(detail=True, methods=['post'])
    def change_status(self, request, pk=None):
        vps = self.get_object()
        new_status = request.data.get('status')
        if new_status in dict(VPS.STATUS_CHOICES):
            vps.status = new_status
            vps.save()
            return Response({'status': 'Status updated successfully'})
        return Response({'error': 'Invalid status'}, status=400)