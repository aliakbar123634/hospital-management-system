from rest_framework import serializers
from . models import *


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=DoctorProfile
        fields=['id','user','specialization','experience_years','qualification','consultation_fee','bio','created_at','updated_at']
        read_only_fields=['id','created_at','updated_at']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Schedule
        fields=['id','doctor','day','start_time','end_time','is_available','created_at','updated_at']
        read_only_fields=['id','created_at','updated_at']
