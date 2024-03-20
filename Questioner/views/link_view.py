from rest_framework.viewsets import ModelViewSet

from Questioner.models import Link
from Questioner.serializers.link_serializer import LinkSerializer


class LinkViewSet(ModelViewSet):
    """Представление для порядка вопросов"""
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
