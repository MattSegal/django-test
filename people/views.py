from rest_framework import viewsets

from .models import Candidate
from .serializers import CandidateSerializer


class CandidateViewSet(viewsets.ReadOnlyModelViewSet):
  """
  Public read only API to view job candidates
  """
  queryset = Candidate.objects.all()
  serializer_class = CandidateSerializer
