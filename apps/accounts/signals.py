from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .utils import generate_unique_username

User = get_user_model()


@receiver(pre_save, sender=User)
def username_add(sender, instance, **kwargs):
    if instance.first_name is not None and instance.last_name is not None:
        username = generate_unique_username(
            instance.first_name + instance.last_name)
    else:
        return
    instance.username = username
