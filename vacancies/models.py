from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=100,  null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    experience_years = models.PositiveIntegerField( null=True, blank=True)
    education = models.CharField(max_length=150, null=True, blank=True)
    skills = models.CharField(max_length=100, null=True, blank=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.full_name