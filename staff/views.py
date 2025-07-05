from rest_framework import viewsets
from .models import FacultyProfile
from .serializers import FacultySerializer

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = FacultyProfile.objects.all()
    serializer_class = FacultySerializer
