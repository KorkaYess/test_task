
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
        Perm for update/destroy objects only by its owners
    """

    def has_object_permission(self, request, view, obj):

        return obj.user == request.user
