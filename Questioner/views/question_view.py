from rest_framework.viewsets import ModelViewSet

from Questioner.models import Question
from Questioner.serializers.question_serializer import QuestionSerializer


class QuestionViewSet(ModelViewSet):
    """Представление для вопросов"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
