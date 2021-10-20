from typing import Tuple
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.IntegerField(null=True, blank=True)
    address=models.CharField(max_length=50,)
    bio=models.TextField(null=True, blank=True)
    profileimage=models.FileField(upload_to="Profilephotos", default="profilephoto.png", null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)
        instance.profile.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()