from rest_framework import permissions


class StudentDataPermissions(permissions.BasePermission):

    """
    Permissions to allow anon users to create data and restrict from viewing it.
    """

    blocked_from_anon = ['GET']
    allowed_to_anon = ['POST']

    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.is_staff:
            return True

        if not request.user.is_authenticated and view.action == "create":
            return True
        elif not request.user.is_authenticated:
            return False


class OnlyOwnerandStaffCanRetrieve(permissions.BasePermission):

    """
    Permissions to allow only the owner to retrieve data.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.is_staff:
            return True

        if request.user.is_authenticated and obj.user == request.user:
            return True
        else:
            return False
