from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.student_data.models import StudentData
from apps.accounts.models import Accounts


class DocumentCategory(models.Model):
    class Meta:
        verbose_name = _("Document Category")
        verbose_name_plural = _("Document Categories")
        ordering = ["id"]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    code = models.CharField(max_length=255, default="00")
    slug = models.SlugField(_('Slug'), max_length=150, unique=True)

    def __str__(self):
        return self.name


def upload_to_path(instance, filename):
    file_name = filename.split(".")[0][:30]
    extension = filename.split(".")[-1]
    path = f'documents/{instance.student_data.first_name}_{instance.student_data.last_name}_{instance.student_data.id}/{file_name}.{extension}'
    return path


class Document(models.Model):

    class Meta:
        verbose_name = _("Document")
        verbose_name_plural = _("Documents")

    student_data = models.ForeignKey(
        StudentData, on_delete=models.CASCADE, related_name='documents')

    category = models.ForeignKey(
        DocumentCategory, on_delete=models.CASCADE, related_name='documents')

    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to=upload_to_path)

    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    checked_by = models.ForeignKey(
        Accounts, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_documents')

    def __str__(self):
        return self.title
