from .serializers import ApplicantSerializer
from .models import Applicant
from rest_framework import filters
from rest_framework import status
from rest_framework import generics

class ApplicantListCreateView(generics.ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['f_name','m_name','l_name']

class ApplicantUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer


