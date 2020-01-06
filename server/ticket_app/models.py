from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=320)
    password = models.CharField(
        validators=[MinLengthValidator(12)], max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
