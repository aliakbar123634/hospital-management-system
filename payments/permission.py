from rest_framework.permissions import BasePermission


class AdminRecipentAllDoctorPatientOwn(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        user=request.user
        if user.role in ["Admin","Receptionist"]:
            return True
        if user.role =="Doctor":
            return obj.appointment.doctor.user==user
        if user.role =="Patient":
            return obj.appointment.patient.user==user        
class AdminResipent(BasePermission):
    def has_permission(self, request, view):
        user=request.user
        return user and user.is_authenticated and user.role in ["Admin","Receptionist"]
    

class BlockUpdateDeletePermission(BasePermission):
    def has_permission(self, request, view):
        # Sirf in actions ko block karo
        if view.action in ["update", "partial_update", "destroy"]:
            return False

        return True    

from rest_framework.permissions import BasePermission


class DoctorPatient(BasePermission):
    def has_permission(self, request, view):
        user=request.user
        return user and user.is_authenticated and user.role in ["Patient" , "Admin"]    

class AdminRecipentallPatientOwn(BasePermission):
    def has_permission(self, request, view):
        user=request.user
        return user and user.is_authenticated and user.role in ["Patient" , "Admin" , "Receptionist"]
    def has_object_permission(self, request, view, obj):
        user=request.user
        if user.role in ["Admin","Receptionist"]:
            return True
        if user.role =="Patient":
            return obj.invoice.appointment.patient.user==user          
        








#              python manage.py runserver    