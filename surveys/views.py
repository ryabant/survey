from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Answer, Survey, Question, Choice
from .serializers import (
    AnswerSerializer,
    ChoiceSerializer,
    SurveySerializer,
    QuestionSerializer,
)


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ("user",)
