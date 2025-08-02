from django.shortcuts import render
from rest_framework import generics
from .models import StudentProfile
from .serializers import StudentProfileSerializer
# Create your views here.

"""
   POST /api/student-onboarding/
   Creates a new student profile with personal, address, and family details.  
"""

class StudentProfileCreateView(generics.CreateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

"""
    GET /api/student-onboarding/<id>/
    Retrieves a student profile by ID.

    PUT /api/student-onboarding/<id>/
    Updates the student profile with the given ID.
"""

class StudentProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    lookup_field = 'id'