from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import DocumentCategory, Document


@admin.register(DocumentCategory)
class DocumentCategoryAdmin(SimpleHistoryAdmin):

    list_display = ('code', 'id', 'name', 'slug')
    search_fields = ('name', 'slug', 'code')
    ordering = ('code',)


@admin.register(Document)
class DocumentAdmin(SimpleHistoryAdmin):

    list_display = ('title', 'category', 'student_data',
                    'uploaded_at', 'is_approved', 'is_rejected', 'checked_by')
    search_fields = ('title', 'description')
    ordering = ('id',)
