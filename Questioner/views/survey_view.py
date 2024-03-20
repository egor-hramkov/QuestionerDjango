from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Questioner.models import Survey
from Questioner.serializers.survey_serializer import SurveySerializer, RetrieveSurveySerializer
from Questioner.utils import prepare_survey_data


class SurveyViewSet(ModelViewSet):
    """Представление для опроса"""
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def retrieve(self, request, *args, **kwargs):
        """Получение опроса с вопросами и ответами"""
        survey = self.get_object()
        serializer = RetrieveSurveySerializer(survey)
        response_data = prepare_survey_data(serializer.data)
        return Response(response_data)
