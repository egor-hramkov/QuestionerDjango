from rest_framework.serializers import ModelSerializer

from Questioner.models import Survey
from Questioner.serializers.question_serializer import QuestionWithAnswersSerializer


class SurveySerializer(ModelSerializer):
    """Сериализитор для опроса"""

    class Meta:
        model = Survey
        fields = '__all__'
        depth = 3


class RetrieveSurveySerializer(SurveySerializer):
    """Сериализатор для полного ответа по опросу"""
    questions = QuestionWithAnswersSerializer(many=True, read_only=True)
