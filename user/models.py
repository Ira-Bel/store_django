from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.PositiveBigIntegerField(null=True, blank=True)
    points = models.SmallIntegerField(blank=True)
    class Meta:
        db_table = "user"
