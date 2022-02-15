from django.contrib import admin
from .models import StudentData
from import_export.admin import ImportExportModelAdmin


@admin.register(StudentData)
class StudentDataAdmin(ImportExportModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name',
                    'destination', 'degree', 'major', 'english_proficiency', 'created')
    list_filter = ('destination', 'degree', 'major', 'english_proficiency')
    search_fields = ('email', 'phone', 'first_name', 'last_name',
                     'destination', 'degree', 'major', 'english_proficiency')
    ordering = ('id',)
