from rest_framework.serializers import ModelSerializer

from Questioner.models import Answer


class AnswerSerializer(ModelSerializer):
    """Сериализитор для Ответов"""

    class Meta:
        model = Answer
        fields = '__all__'


class AnswerWithoutRelationsSerializer(ModelSerializer):
    """Серализатор для ответов без связки с вопросами """

    class Meta:
        model = Answer
        exclude = ('question',)
