from rest_framework import serializers
from . models import PatientProfile , MedicalHistory


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=PatientProfile
        fields=['id','user','gender','date_of_birth','blood_group','address','emergency_contact','created_at','updated_at']
        read_only_fields=['id','created_at','updated_at']

class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicalHistory
        fields=['id' , 'patient','disease','allergies','medications','notes','record_date','created_at','updated_at']
        read_only_fields=['id','created_at','updated_at']