from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Questioner.models import Survey
from Questioner.serializers.survey_serializer import SurveySerializer, RetrieveSurveySerializer


class SurveyViewSet(ModelViewSet):
    """Представление для опроса"""
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def retrieve(self, request, *args, **kwargs):
        """Получение опроса с вопросами и ответами"""
        survey = self.get_object()
        serializer = RetrieveSurveySerializer(survey)
        return Response(serializer.data)
