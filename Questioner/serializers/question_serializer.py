from rest_framework.serializers import ModelSerializer

from Questioner.models import Question
from Questioner.serializers.answer_serializer import AnswerWithoutRelationsSerializer


class QuestionSerializer(ModelSerializer):
    """Сериализитор для вопросов"""

    class Meta:
        model = Question
        fields = '__all__'


class QuestionWithAnswersSerializer(QuestionSerializer):
    """Сериализатор для вопроса с ответами"""
    answers = AnswerWithoutRelationsSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        exclude = ('survey',)
