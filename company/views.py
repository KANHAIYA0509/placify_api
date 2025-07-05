from rest_framework import viewsets
from .models import CompanyProfile
from .serializers import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanySerializer
