from django.urls import path
from .views import StudentProfileCreateView, StudentProfileDetailView

urlpatterns = [
    path('student-onboarding/', StudentProfileCreateView.as_view()),
    path('student-onboarding/<int:id>/', StudentProfileDetailView.as_view()),
]