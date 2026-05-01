from rest_framework import serializers
from . models import *



class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Prescription
        fields=['id','appointment','diagnosis','medicines','dosage','instructions','created_at', 'updated_at']
        read_only_fields=['id','created_at', 'updated_at']

class MedicalReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicalReport
        fields=['id','patient','prescription','report_type','report_file','remarks','created_at', 'updated_at']
        read_only_fields=['id','created_at', 'updated_at']        




#             python manage.py runserver        