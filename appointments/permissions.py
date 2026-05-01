from rest_framework.permissions import BasePermission

class AdminAllDcotorParientOwn(BasePermission):
    def has_permission(self, request, view):
        user=request.user
        return user and user.is_authenticated and user.role in ["Admin","Doctor","Patient"]
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.role == "Admin":
            return True
        if user.role == "Doctor":
            return obj.doctor.user == request.user
        if user.role == "Patient":
            return obj.patient.user == request.user        
        return False  


class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        user=request.user
        return user and user.is_authenticated and user.role=="Doctor"