from rest_framework import permissions
from rest_framework.views import Request, View


#class IsSuperUser(permissions.BasePermission):
#    def has_permission(self, request: Request, view: View) -> bool:
#        return request.is_employee == request.is_superUser
