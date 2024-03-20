from rest_framework.viewsets import ModelViewSet

from Questioner.models import Answer
from Questioner.serializers.answer_serializer import AnswerSerializer


class AnswerViewSet(ModelViewSet):
    """Представление для ответов"""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
