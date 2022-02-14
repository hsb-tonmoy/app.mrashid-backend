from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.dispatch import receiver
from .utils import generate_unique_username

User = get_user_model()


@receiver(pre_save, sender=User)
def username_add(sender, instance, **kwargs):
    if instance.first_name and instance.last_name:
        username = generate_unique_username(
            instance.first_name + instance.last_name)
    else:
        return
    instance.username = username


@receiver(pre_save, sender=User)
def add_or_update_user_group(sender, instance, created, **kwargs):
    if created:
        if instance.account_type == 1:
            if not Group.objects.filter(name="Students").exists():
                Group.objects.create(name="Students")
            group = Group.objects.get(name="Students")

        elif instance.account_type == 2:
            if not Group.objects.filter(name="Consultants").exists():
                Group.objects.create(name="Consultants")
            group = Group.objects.get(name="Consultants")

        elif instance.account_type == 3:
            if not Group.objects.filter(name="Managers").exists():
                Group.objects.create(name="Managers")
            group = Group.objects.get(name="Managers")

        elif instance.account_type == 4:
            if not Group.objects.filter(name="Admins").exists():
                Group.objects.create(name="Admins")
            group = Group.objects.get(name="Admins")

        elif instance.is_superuser:
            if not Group.objects.filter(name="Admin").exists():
                Group.objects.create(name="Admin")
            group = Group.objects.get(name="Admin")
            instance.account_type == 5

        instance.groups.add(group)
