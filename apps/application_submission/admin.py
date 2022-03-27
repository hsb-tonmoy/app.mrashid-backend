from django.db import models
from django.contrib import admin
from .models import PreApplicationForm
from simple_history.admin import SimpleHistoryAdmin


@admin.register(PreApplicationForm)
class PreApplicationFormAdmin(SimpleHistoryAdmin):

    list_display = ('id', 'student')
