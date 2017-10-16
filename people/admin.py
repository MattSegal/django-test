from django.contrib import admin

from .models import Candidate


class CandidateAdmin(admin.ModelAdmin):
  readonly_fields = ('uuid',)

admin.site.register(Candidate, CandidateAdmin)
