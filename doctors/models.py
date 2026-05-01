from django.db import models
from accounts.models import CustomUserModel
# Create your models here.

class DoctorProfile(models.Model):
    role=(
        ('Male' , 'Male'),
        ('Female' , 'Female'),
        ('Others' , 'Others')
    ) 
    user=models.OneToOneField(CustomUserModel , on_delete=models.CASCADE , related_name="doctorprofile")
    specialization=models.CharField(max_length=10 , null=True , blank=True)
    experience_years=models.IntegerField()
    qualification=models.CharField(max_length=10 , null=True , blank=True)
    consultation_fee=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bio=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True) 


class Schedule(models.Model):
    doctor=models.ForeignKey(DoctorProfile , on_delete=models.CASCADE , related_name="schedule")  
    day=models.CharField(max_length=25)
    start_time=models.TimeField()
    end_time=models.TimeField()
    is_available=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)    
    def __str__(self):
        return f"{self.doctor} - {self.day} ({self.start_time} - {self.end_time})"    