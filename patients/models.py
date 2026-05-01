from django.db import models
from accounts.models import CustomUserModel
# Create your models here.

class PatientProfile(models.Model):
    role=(
        ('Male' , 'Male'),
        ('Female' , 'Female'),
        ('Others' , 'Others')
    ) 
    user=models.OneToOneField(CustomUserModel , on_delete=models.CASCADE , related_name="patientprofile")
    gender=models.CharField(max_length=15 , choices=role , default='Male')
    date_of_birth=models.DateField(blank=True , null=True)
    blood_group=models.CharField(max_length=10 , null=True , blank=True)
    address=models.TextField()
    emergency_contact=models.CharField(max_length=10 , null=True , blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)    

class MedicalHistory(models.Model):
    patient=models.ForeignKey(PatientProfile , on_delete=models.CASCADE , related_name="medicalhistory")
    disease=models.CharField(max_length=255)
    allergies=models.TextField()
    medications=models.TextField()
    notes=models.TextField()
    record_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)     