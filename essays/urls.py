from django.urls import path
from .views import EssayCreateView, EssayVersionView, LatestEssayVersionView
urlpatterns = [
    path('essays/', EssayCreateView.as_view()),
    path('essays/<int:essay_id>/versions/', EssayVersionView.as_view()),
    path('essays/<int:essay_id>/latest-version/', LatestEssayVersionView.as_view()),
]