from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('job_seeker', 'Соискатель'),
        ('employer', 'Работодатель'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='job_seeker'
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"