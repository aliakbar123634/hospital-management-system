from . serializers import PatientSerializer  , MedicalHistorySerializer
from . models import PatientProfile , MedicalHistory
from rest_framework.viewsets import ModelViewSet
from . permissions import DoctorRecipentAndAdmin, OnlyPatientPermission , OwnPatient , OwnPatientAndDoctor , DoctorRecipent , AllUser , AdminRecipent , AdminOnly
from rest_framework.permissions import AllowAny
# Create your views here.


class PatientModelViewSet(ModelViewSet):
    queryset=PatientProfile.objects.all()
    serializer_class=PatientSerializer
    # parser_classes=[AllowAny]
    permission_classes=[AllowAny]
    def get_permissions(self):
        if self.action == "create":
            return [OnlyPatientPermission()]
        if self.action == "reterieve":
            return [OwnPatientAndDoctor()]    
        if self.action in ["put" , "destory"]:
            return [OwnPatient()]      
        return super().get_permissions()

    

class MedicalHistoryViewSet(ModelViewSet):
    queryset=MedicalHistory.objects.all()
    serializer_class=MedicalHistorySerializer
    def get_permissions(self):
        if self.action == "create":
            return [DoctorRecipent()]
        if self.action=="list":
            return [DoctorRecipentAndAdmin()]    
        if self.action=="reterieve":
            return [AllUser()] 
        if self.action=="put":
            return [AdminRecipent()] 
        if self.action in ["destory"]:
            return [OwnPatient()] 
        return super().get_permissions()                        
    def get_queryset(self):
        user = self.request.user
        if user.role == "Admin":
            return MedicalHistory.objects.all()
        elif user.role == "Doctor":
            return MedicalHistory.objects.filter(
                patient__appointment__doctor__user=user
        ).distinct() 
        elif user.role == "Patient":
            return MedicalHistory.objects.filter(
                patient__user=user
        )       
        return MedicalHistory.objects.none()
    




#        python manage.py runserver            
