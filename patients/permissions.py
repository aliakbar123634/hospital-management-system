from rest_framework.permissions import BasePermission


class OnlyPatientPermission(BasePermission):
    def has_permission(self, request, view):
        user=request.user
        return user and user.is_authenticated and user.role=="Patient"
    
class OwnPatientAndDoctor(BasePermission):
    def has_permission(self, request, view):
        user=request.user
        return user and user.is_authenticated and user.role in ["Patient" , "Doctor"]
    def has_object_permission(self, request, view, obj):
        return obj.user==request.user
class OwnPatient(BasePermission):            
    def has_object_permission(self, request, view, obj):
        return obj.user==request.user    
    
class DoctorRecipent(BasePermission):
    def has_permission(self, request, view):
        user=request.user
        return user and user.is_authenticated and user.role in ["Receptionist" , "Doctor"]   
class DoctorRecipentAndAdmin(BasePermission):
    def has_permission(self, request, view):
        user=request.user
        return user and user.is_authenticated and user.role in ["Admin", "Receptionist", "Doctor"]  
    
class AllUser(BasePermission):    
    def has_permission(self, request, view):
        user=request.user
        return user and user.is_authenticated and user.role in ["Admin", "Receptionist", "Doctor","Patient"]      

class AdminRecipent(BasePermission):
    def has_permission(self, request, view):
        user=request.user
        return user and user.is_authenticated and user.role in ["Admin", "Receptionist"] 
class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        user=request.user
        return user and user.is_authenticated and user.role == "Admin"