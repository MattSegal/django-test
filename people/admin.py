from django.contrib import admin

from .models import Candidate

# make UUID read only
# Add 'optional' to is_citizen
class CandidateAdmin(admin.ModelAdmin):
  readonly_fields = ('uuid',)

admin.site.register(Candidate, CandidateAdmin)
