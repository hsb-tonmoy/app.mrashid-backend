from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .utils import random_username, generate_unique_username

User = get_user_model()


@receiver(pre_save, sender=User)
def username_add(sender, instance, **kwargs):
    if instance.first_name and instance.last_name:
        username = generate_unique_username(
            instance.first_name + instance.last_name)
    else:
        return
    instance.username = username
