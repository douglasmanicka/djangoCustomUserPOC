from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Account(AbstractUser):
    ACCOUNT_TYPES = (
        (u'T', u'Teacher'),
        (u'A', u'administrative'),
    )
    type = models.CharField(max_length=14, choices=ACCOUNT_TYPES)
    
