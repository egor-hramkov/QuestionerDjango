from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Questioner.views import QuestionViewSet, AnswerViewSet, SurveyViewSet, LinkViewSet

router = DefaultRouter()
router.register(r'surveys', SurveyViewSet, basename='survey')
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'answers', AnswerViewSet, basename='answer')
router.register(r'links', LinkViewSet, basename='links')

urlpatterns = [
    path('', include(router.urls)),
]
