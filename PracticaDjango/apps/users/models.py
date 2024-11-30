from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    company = models.ForeignKey('sistemas.Empresa', related_name='company_user', on_delete=models.CASCADE)