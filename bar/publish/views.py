from rest_framework import viewsets

from .serializers import PublishSerializer
from .models import Publish


class PublishViewSet(viewsets.ModelViewSet):
    queryset = Publish.objects.all().order_by('id')
    serializer_class = PublishSerializer
