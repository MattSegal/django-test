from django.contrib import admin

from .models import Candidate

# make UUID read only
# Add 'optional' to is_citizen

admin.site.register(Candidate)
