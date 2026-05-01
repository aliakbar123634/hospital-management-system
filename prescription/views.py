from django.shortcuts import render
from . serializers import *
from . models import *
from rest_framework.viewsets import ModelViewSet
from . permissions import DoctorAdmin , AdminAllDoctorPatientOwn
from rest_framework.permissions import IsAuthenticated , AllowAny
from patients.permissions import AdminOnly
# Create your views here.

class PrescriptionViewSet(ModelViewSet):
    queryset=Prescription.objects.all()
    serializer_class=PrescriptionSerializer
    def get_permissions(self):
        if self.action==["create" , "update" , "partial_update"]:
            return [DoctorAdmin()] 
        if self.action in ["retrieve", "list"]:
            return [AdminAllDoctorPatientOwn()]       
        return super().get_permissions()
    def get_queryset(self):
        user = self.request.user
        if user.role == "Admin":
            return Prescription.objects.all()
        elif user.role == "Doctor":
            return Prescription.objects.filter(
            appointment__doctor__user=user
        )
        elif user.role == "Patient":
            return Prescription.objects.filter(
            appointment__patient__user=user
        )

        return Prescription.objects.none()



class MedicalReportViewSet(ModelViewSet):
    queryset=MedicalReport.objects.all()
    serializer_class=MedicalReportSerializer
    permission_classes=[IsAuthenticated]
    permission_classes=[AdminAllDoctorPatientOwn] 
    def get_permissions(self):
        if self.action in ["create" , "update" , "partial_update"]:
            return [DoctorAdmin()]   
        if self.action in ["destroy"]:
            return [AdminOnly()]                 
        return super().get_permissions()
    def get_queryset(self):
        user=self.request.user
        if user.role=="Admin":
            return MedicalReport.objects.all()
        elif user.role=="Doctor":
            return MedicalReport.objects.filter(
                prescription__appointment__doctor__user=user
            )
        elif user.role=="Patient":
            return MedicalReport.objects.filter(
                prescription__appointment__patient__user=user
            )
        
        return MedicalReport.objects.none()