from rest_framework import serializers

from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
  resume_data = serializers.ReadOnlyField()
  resume_sha256 = serializers.ReadOnlyField()
  resume_encoding = serializers.ReadOnlyField()

  class Meta:
    model = Candidate
    fields = (
      'real_name',
      'birth_date',
      'is_citizen',
      'description',
      'favourite_language',
      'years_experience',
      'photo',
      'resume_data',
      'resume_encoding',
      'resume_sha256',
      'uuid',
    )

