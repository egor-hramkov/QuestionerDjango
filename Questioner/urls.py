from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Questioner.views import QuestionViewSet, AnswerViewSet, SurveyViewSet

router = DefaultRouter()
router.register(r'surveys', SurveyViewSet, basename='survey')
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'answers', AnswerViewSet, basename='answer')

urlpatterns = [
    path('', include(router.urls)),
]
