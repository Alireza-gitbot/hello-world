from rest_framework.permissions import BasePermission


class UserOk(BasePermission):

    def has_permission(self, request, view):
        message = "just admin user see this View"
        user = User.objects.filter(name='admin')
        if user is True:
            return user
        return False