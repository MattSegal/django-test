import base64
import uuid
import os
from hashlib import sha256

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
  photo = models.FileField(upload_to='photos')
  resume = models.FileField(upload_to='resume')
  uuid = models.UUIDField(default=uuid.uuid4)

  def __str__(self):
    return '{} ({})'.format(self.real_name, self.uuid)

  def resume_data(self):
    return base64.b64encode(self.resume.read())

  def resume_encoding(self):
    return 'base64'

  def resume_hash(self):
    resume_bytes = b'woo this is some bytes'
    return sha256(resume_bytes).hexdigest()