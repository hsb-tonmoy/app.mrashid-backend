import json
from django.db import models
from django import forms
from django.contrib import admin
from .models import StudentData
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin


class JSONEditorWidget(forms.Widget):

    def __init__(self, attrs=None) -> None:
        super(JSONEditorWidget, self).__init__(attrs=attrs)

    template_name = 'student_data/django_json_widget.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['value'] = json.loads(value)

        return context


@admin.register(StudentData)
class StudentDataAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }

    list_display = ('id', 'email', 'first_name', 'last_name',
                    'destination', 'degree', 'major', 'english_proficiency', 'created', 'status', 'rating')
    list_filter = ('destination', 'degree', 'major',
                   'english_proficiency', 'status', 'rating')
    search_fields = ('email', 'phone', 'first_name', 'last_name',
                     'destination', 'degree', 'major', 'english_proficiency')
    ordering = ('-rating',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.exclude(status=4)
        return queryset
