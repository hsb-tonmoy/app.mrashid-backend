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
    middle_initials = models.CharField(
        _("Middle Initials"), max_length=255, blank=True, null=True)
    last_name = models.CharField(_("Last Name"), max_length=255)
    email = models.EmailField(_("Email"), max_length=255, unique=True)
    phone = models.CharField(_("Phone"), max_length=255)
    social_media = models.CharField(
        _("Social Media"), max_length=255, blank=True, null=True)

    address_line_1 = models.CharField(
        _("Address Line 1"), max_length=255, blank=True, null=True)
    address_line_2 = models.CharField(
        _("Address Line 2"), max_length=255, blank=True, null=True)
    city = models.CharField(_("City"), max_length=255, blank=True, null=True)
    state = models.CharField(_("State"), max_length=255, blank=True, null=True)
    zip_code = models.CharField(
        _("Zip Code"), max_length=255, blank=True, null=True)
    country = models.CharField(
        _("Country"), max_length=255, blank=True, null=True)

    date_of_birth = models.DateField(_("Date of Birth"), blank=True, null=True)
    gender = models.CharField(
        _("Gender"), max_length=100, null=True, blank=True)
    marital_status = models.CharField(
        _("Marital Status"), max_length=255, blank=True, null=True)

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


class StudentProgress(models.Model):
    class Meta:
        verbose_name = _("Student Progress")
        verbose_name_plural = _("Student Progress")

    history = HistoricalRecords()

    student_data = models.OneToOneField(
        StudentData, on_delete=models.CASCADE, related_name="progress")

    STEP_STATUS = (
        (1, 'Pending'),
        (2, 'Incomplete'),
        (3, 'Completed'),
    )

    account_creation = models.PositiveSmallIntegerField(
        _("Account Creation"), choices=STEP_STATUS, default=1)

    file_opening = models.PositiveSmallIntegerField(
        _("File Opening"), choices=STEP_STATUS, default=1)

    docu_submission = models.PositiveSmallIntegerField(
        _("Submission of Documents"), choices=STEP_STATUS, default=1)

    application_submission = models.PositiveSmallIntegerField(
        _("Submission of Application"), choices=STEP_STATUS, default=1)

    i20_reception = models.PositiveSmallIntegerField(
        _("Receipt of I-20"), choices=STEP_STATUS, default=1)

    sevis_payment = models.PositiveSmallIntegerField(
        _("SEVIS Payment"), choices=STEP_STATUS, default=1)

    ds160_submission = models.PositiveSmallIntegerField(
        _("Submission of DS-160"), choices=STEP_STATUS, default=1)

    visa_fee = models.PositiveSmallIntegerField(
        _("Visa Processing Fee Payment"), choices=STEP_STATUS, default=1)

    visa_interview = models.PositiveSmallIntegerField(
        _("Visa Interview Preparation"), choices=STEP_STATUS, default=1)

    visa_collection = models.PositiveSmallIntegerField(
        _("Visa Collection"), choices=STEP_STATUS, default=1)

    pre_dept_session = models.PositiveSmallIntegerField(
        _("Pre-departure Session"), choices=STEP_STATUS, default=1)

    welcoming_in_us = models.PositiveSmallIntegerField(
        _("Welcoming in the USA"), choices=STEP_STATUS, default=1)
