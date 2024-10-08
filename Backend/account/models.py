from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# Custom User model
class User(AbstractUser):
    pass  # No need for is_customer or is_expert fields


# User Profile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    resume = models.FileField(null=True)


# Signal to create UserProfile when a User is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# Customer model linked to User
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


# Expert model linked to User
class Expert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
