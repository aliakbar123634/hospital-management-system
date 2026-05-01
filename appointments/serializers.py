from rest_framework import serializers
from . models import Appointment

class AppointmentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields=['id' , 'patient','doctor','schedule','appointment_date','status','reason','notes','created_at','updated_at']
        read_only_fields=['id','created_at','updated_at']        