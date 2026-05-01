from rest_framework.permissions import BasePermission


class AdminAllAndDoctorOwn(BasePermission):
    def has_permission(self, request, view):
        user=request.user
        return user and user.is_authenticated and user.role in ["Admin","Doctor"]

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.role == "Admin":
            return True
        if user.role == "Doctor":
            return obj.user == user
        return False
class AdminAllDoctorOwnSchedule(BasePermission):
    def has_permission(self, request, view):
        user=request.user
        return user and user.is_authenticated and user.role in ["Admin","Doctor"] 
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.role == "Admin":
            return True
        if user.role == "Doctor":
            return obj.doctor.user == request.user
        return False        