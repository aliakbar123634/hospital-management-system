from rest_framework.viewsets import ModelViewSet
from . models import DoctorProfile , Schedule
from . serializers import DoctorSerializer , ScheduleSerializer
from rest_framework.permissions import AllowAny
from .permissions import AdminAllAndDoctorOwn , AdminAllDoctorOwnSchedule
from patients.permissions import AdminOnly
from rest_framework_simplejwt.authentication import JWTAuthentication 

# Create your views here.
class DoctorViewSet(ModelViewSet):
    queryset=DoctorProfile.objects.all()
    serializer_class=DoctorSerializer
    permission_classes=[AllowAny]
    
    def get_permissions(self):
        if self.action in ["create" , "destroy"]:
            return [AdminOnly()]
        if self.action in ["update", "partial_update"]:
            return [AdminAllAndDoctorOwn()]
        return super().get_permissions()
    
class ScheduleModelViewSet(ModelViewSet):
    queryset=Schedule.objects.all()
    serializer_class=ScheduleSerializer
    permission_classes=[AllowAny]
    authentication_classes = [JWTAuthentication]
    
    def get_permissions(self):
        # if self.action in ["create" ,  "update", "partial_update"]:
        #     return [AdminAllDoctorOwnSchedule()]
        if self.action == "destroy":
            return [AdminOnly()]                
        return super().get_permissions()



        #                       python manage.py runserver