from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any custom fields if needed
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Example custom field

    def __str__(self):
        return self.username
