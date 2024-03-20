from rest_framework.serializers import ModelSerializer

from Questioner.models import Link


class LinkSerializer(ModelSerializer):
    """Сериализатор для порядка вопросов"""

    class Meta:
        model = Link
        fields = '__all__'
