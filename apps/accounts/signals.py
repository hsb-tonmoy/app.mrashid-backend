from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .utils import generate_unique_username

User = get_user_model()


@receiver(pre_save, sender=User)
def username_add(sender, instance, **kwargs):
    if instance.username is 'username':
        if instance.firstname is not None and instance.lastname is not None:
            username = generate_unique_username(
                instance.firstname + instance.lastname)
        else:
            username = None
        instance.username = username
