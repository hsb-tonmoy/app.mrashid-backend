from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Note, NoteCategory

admin.site.register(NoteCategory)


@admin.register(Note)
class NoteAdmin(SimpleHistoryAdmin):
    model = Note
    list_display = ('student', 'title', 'category', 'internal', 'complete',
                    'priority', 'date_added', 'created_by',)
    fieldsets = (
        (None, {'fields': ('student', 'title', 'description', 'category',
         'internal', 'complete', 'date_modified', 'priority', 'date_added', 'created_by')}),
    )
    readonly_fields = ('date_added', 'date_modified',)
