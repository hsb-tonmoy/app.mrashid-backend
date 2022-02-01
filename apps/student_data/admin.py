from django.contrib import admin
from .models import StudentData


@admin.register(StudentData)
class StudentDataAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name',
                    'destination', 'degree', 'major', 'english_proficiency')
    list_filter = ('destination', 'degree', 'major', 'english_proficiency')
    search_fields = ('email', 'phone', 'first_name', 'last_name',
                     'destination', 'degree', 'major', 'english_proficiency')
    ordering = ('id',)
