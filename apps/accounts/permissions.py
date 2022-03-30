from rest_framework import permissions


class OnlyAdminandStaffCanRetrieve(permissions.BasePermission):

    """
    Permissions to allow only the admins and staff to retrieve data.
    """

    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False
