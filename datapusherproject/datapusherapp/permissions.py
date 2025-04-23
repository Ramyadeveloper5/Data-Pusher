from rest_framework import permissions

class IsAdminUserForAccount(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.accountmember_set.filter(account=obj, role__role_name='Admin').exists()

class IsMemberOfAccount(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.accountmember_set.filter(account=obj).exists()
