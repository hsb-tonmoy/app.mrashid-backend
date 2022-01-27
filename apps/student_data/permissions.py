from asyncio.format_helpers import _format_callback_source
from rest_framework.permissions import BasePermission


class StudentDataPermissions(BasePermission):

    blocked_from_anon = ['GET']
    allowed_to_anon = ['POST']

    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.is_staff:
            return True

        if not request.user.is_authenticated and request.method in self.blocked_from_anon:
            return False

        if not request.user.is_authenticated and request.method in self.allowed_to_anon:
            return True
