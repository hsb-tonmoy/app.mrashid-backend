from django.contrib import admin
from .models import Note, NoteCategory

admin.site.register(NoteCategory)
admin.site.register(Note)
