from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from surveys.views import QuestionViewSet, SurveyViewSet

router = DefaultRouter()

router.register(r"surveys", SurveyViewSet)
router.register(r"questions", QuestionViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
]
