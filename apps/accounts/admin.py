from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from simple_history.admin import SimpleHistoryAdmin

from .models import Accounts


class AccountsAdmin(UserAdmin, SimpleHistoryAdmin):
    model = Accounts
    list_display = ('student', 'email', 'first_name', 'last_name',
                    'is_staff', 'is_active',)
    list_filter = ('email', 'first_name', 'last_name',
                   'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('student', 'email', 'username',
         'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('account_type', 'is_staff', 'is_active')}),
        ('Other', {'fields': ('date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('student', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active', 'account_type')}
         ),
    )
    search_fields = ('email', 'first_name', 'last_name',)
    ordering = ('id',)


admin.site.register(Accounts, AccountsAdmin)
