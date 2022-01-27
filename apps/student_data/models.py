from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class StudentData(models.Model):

    class Meta:
        verbose_name = _("Student Data")
        verbose_name_plural = _("Student Data")
        ordering = ["id"]

    created = models.DateTimeField(_("Created at"), default=timezone.now)

    # Destination

    destination = models.CharField(_("Destination"), max_length=255)

    # Degree

    degree = models.CharField(_("Degree"), max_length=255)

    # Personal Information

    firstname = models.CharField(_("First Name"), max_length=255)
    lastname = models.CharField(_("Last Name"), max_length=255)
    email = models.EmailField(_("Email"), max_length=255)
    phone = models.CharField(_("Phone"), max_length=255)
    social_media = models.CharField(_("Social Media"), max_length=255)

    # Major

    major = models.CharField(_("Major"), max_length=255)

    # Education

    education = models.JSONField(_("Education"))

    # English Proficiency

    ielts = models.CharField(_("IELTS"), max_length=255)

    # Message

    message = models.TextField(
        _("Message"), max_length=255, blank=True, null=True)

    def __str__(self):
        return self.firstname + " " + self.lastname
