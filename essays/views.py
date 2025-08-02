from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import Essay, EssayVersion
from rest_framework.response import Response
from .serializers import EssaySerializer, EssayVersionSerializer
# Create your views here.


class EssayCreateView(generics.CreateAPIView):
    """
    POST /api/essays/
    Create a new essay with student_id, college_name, and question_title.
    """
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer

class EssayVersionView(APIView):
    """
    GET /api/essays/<essay_id>/versions/ - List all versions for an essay
    POST /api/essays/<essay_id>/versions/ - Upload a new essay version with file
    """

    def get(self, request, essay_id):
        versions = EssayVersion.objects.filter(essay_id=essay_id)
        serializer = EssayVersionSerializer(versions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, essay_id):
        try:
            essay = Essay.objects.get(id=essay_id)
        except Essay.DoesNotExist:
            return Response({"error": "Essay not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = EssayVersionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(essay=essay)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LatestEssayVersionView(generics.RetrieveAPIView):
    """
    GET /api/essays/<essay_id>/latest-version/
    Retrieve the most recently submitted essay version for the given essay.
    """
    serializer_class = EssayVersionSerializer

    def get_object(self):
        essay_id = self.kwargs['essay_id']
        return EssayVersion.objects.filter(essay_id=essay_id).latest('submitted_at')


