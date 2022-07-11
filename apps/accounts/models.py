from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from simple_history.models import HistoricalRecords
from .utils import random_username
from random import randint
from .managers import AccountsManager

from apps.student_data.models import StudentData


def upload_to_path(instance, filename):
    extension = filename.split(".")[-1].lower()
    file_id = randint(10000000, 99999999)
    path = f'profiles/{file_id}_{instance.last_name}.png'
    return path


class Accounts(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")
        ordering = ["id"]

    objects = AccountsManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    history = HistoricalRecords()

    # General fields

    email = models.EmailField(_('Email Address'), unique=True)

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("A user with that username already exists."),

        },
        blank=True,
        default=random_username
    )
    profile_pic = ProcessedImageField(upload_to=upload_to_path,
                                      processors=[ResizeToFill(270, 270)],
                                      format='PNG',
                                      options={'quality': 60}, default='profiles/avatar.png', null=True, blank=True)
    first_name = models.CharField(_('First name'), max_length=150, blank=True)
    last_name = models.CharField(_('Last name'), max_length=150, blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USER_TYPE_CHOICES = (
        (1, 'Visitor'),
        (2, 'Client'),
        (3, 'Consultant'),
        (4, 'Manager'),
        (5, 'Admin'),
        (6, 'SuperAdmin'),
    )

    account_type = models.PositiveSmallIntegerField(
        _("Account Type"), choices=USER_TYPE_CHOICES, default=1)

    # Relationships

    student = models.OneToOneField(
        StudentData, on_delete=models.SET_NULL, related_name="user", null=True, blank=True)

    # Model methods

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name


class ClientFollowing(models.Model):
    manager = models.ForeignKey(
        Accounts, related_name="clients", on_delete=models.CASCADE)
    client = models.ForeignKey(
        Accounts, related_name="managers", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['manager', 'client'],  name="unique_followers")
        ]

        ordering = ["-created"]

    def __str__(self):
        return f'{self.manager.first_name} following {self.client.first_name}'
