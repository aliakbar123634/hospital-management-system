from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . serializers import *
from . models import *
from rest_framework.permissions import IsAuthenticated
from . permissions import AdminAllDcotorParientOwn , IsDoctor
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class AppointmentViewSet(ModelViewSet):
    queryset=Appointment.objects.all()
    serializer_class=AppointmentSerializers
    permission_classes=[IsAuthenticated]
    def get_permissions(self):
        if self.action=="retrieve":
            return [AdminAllDcotorParientOwn()]
        return super().get_permissions()  
    @action(detail=True , methods=['PATCH'] , url_path="status" , permission_classes=[IsDoctor])
    def status_change(self , request , pk=None):
        try:
            app=Appointment.objects.get(id=pk)
        except Appointment.DoesNotExist:
            return Response({
                "message":"Appointment does not exist at this id"
            })    
        status_value=request.data.get("status")
        app.status=status_value
        app.save()
        return Response({
            "status":app.status,
            "message":"Status updated successfully .........."
        },status=status.HTTP_200_OK)
    @action(detail=True , methods=['PATCH'] , url_path="cancel" , permission_classes=[AdminAllDcotorParientOwn])     
    def Cancel_Appointment(self , request , pk=None):
        try:
            app=Appointment.objects.get(id=pk)
        except Appointment.DoesNotExist:
            return Response({
                "message":"Appointment does not exist at this id"
            }) 
        app.status="cancelled"
        app.save()
        return Response({
            "status":app.status,
            "message":"Status updated successfully .........."
        },status=status.HTTP_200_OK)



#        python manage.py runserver
