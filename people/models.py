import uuid
from django.db import models


class Candidate(models.Model):

  LANGUAGE_CHOICES = (
    ('PYT', 'Python'),
    ('PHP', 'PHP'),
    ('PRL', 'Perl'),
    ('PLG', 'Prolog'),
    ('FTN', 'Fortran'),
    ('HKL', 'Haskell'),
  )

  real_name = models.CharField(max_length=250)
  birth_date = models.DateField()
  is_citizen = models.BooleanField(blank=True)
  description = models.TextField()
  favourite_language = models.CharField(
    max_length=3,
    choices=LANGUAGE_CHOICES,
  )
  years_experience = models.PositiveIntegerField()
  #photo = models.FileField()
  resume = models.TextField()
  resume_hash = models.CharField(max_length=64)
  uuid = models.UUIDField(default=uuid.uuid4)

  def __str__(self):
    return '<Candidate {} ({})>'.format(self.real_name, self.uuid)
