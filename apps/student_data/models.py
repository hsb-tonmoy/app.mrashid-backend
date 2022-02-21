from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords
from django.utils import timezone


class StudentData(models.Model):

    class Meta:
        verbose_name = _("Student Data")
        verbose_name_plural = _("Student Data")
        ordering = ["-rating"]

    history = HistoricalRecords()

    created = models.DateTimeField(_("Created at"), default=timezone.now)

    # Destination

    destination = models.CharField(_("Destination"), max_length=255)

    # Degree

    degree = models.CharField(_("Degree"), max_length=255)

    # Personal Information

    first_name = models.CharField(_("First Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255)
    email = models.EmailField(_("Email"), max_length=255, unique=True)
    phone = models.CharField(_("Phone"), max_length=255)
    social_media = models.CharField(
        _("Social Media"), max_length=255, blank=True, null=True)

    # Major

    major = models.CharField(_("Major"), max_length=255)

    # Education

    education = models.JSONField(_("Education"))

    # English Proficiency

    EP_CHOICES = [
        ('ielts', 'IELTS'),
        ('toefl', 'TOEFL'),
        ('duolingo', 'Duolingo'),
        ('no-test', 'Wish to get enrolled without any test'),
        ('moi', 'Wish to get enrolled with Medium Of Instruction'),
        ('plan-to', 'Wish to take IELTS'),
    ]

    english_proficiency = models.CharField(
        _("English Proficiency"), max_length=15, choices=EP_CHOICES, default='ielts')

    english_proficiency_score = models.CharField(
        _("Score"), max_length=255, blank=True, null=True)

    # Message

    message = models.TextField(
        _("Message"), blank=True, null=True)

    dr_rashids_notes = models.TextField(
        _("Dr. Rashid's Notes"), blank=True, null=True)

    # Internal Fields

    STATUS_CHOICES = (
        (0, "Default"),
        (1, "Package Sent"),
        (2, "Converted"),
        (3, "Follow-up"),
        (4, "Muted"),
    )

    status = models.PositiveSmallIntegerField(
        _("Status"), choices=STATUS_CHOICES, default=0)

    PRIORITY_RATINGS = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )

    rating = models.PositiveSmallIntegerField(
        _("Rating"), choices=PRIORITY_RATINGS, default=1)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def is_converted(self):
        return self.status == 2

    def is_muted(self):
        return self.status == 4
