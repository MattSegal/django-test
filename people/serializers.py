from rest_framework import serializers

from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Candidate
    fields = (
      'real_name',
      'birth_date',
      'is_citizen',
      'description',
      'favourite_language',
      'years_experience',
      # 'photo',
      'resume',
      'resume_hash',
      'uuid',
    )
