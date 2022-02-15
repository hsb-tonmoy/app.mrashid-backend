import json
from django.db import models
from django import forms
from django.contrib import admin
from .models import StudentData
from import_export.admin import ImportExportModelAdmin
from django.utils.safestring import mark_safe


class JSONEditorWidget(forms.Widget):

    def __init__(self, attrs=None) -> None:
        super(JSONEditorWidget, self).__init__(attrs=attrs)

    template_name = 'student_data/django_json_widget.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        return context


@admin.register(StudentData)
class StudentDataAdmin(ImportExportModelAdmin):
    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.JSONField: {'widget': JSONEditorWidget},
    }

    list_display = ('id', 'email', 'first_name', 'last_name',
                    'destination', 'degree', 'major', 'english_proficiency', 'created')
    list_filter = ('destination', 'degree', 'major', 'english_proficiency')
    search_fields = ('email', 'phone', 'first_name', 'last_name',
                     'destination', 'degree', 'major', 'english_proficiency')
    ordering = ('id',)
