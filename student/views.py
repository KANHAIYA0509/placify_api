from rest_framework import viewsets
from .models import StudentProfile
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentSerializer
