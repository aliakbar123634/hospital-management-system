from django.db import models
from patients.models import PatientProfile    
from doctors.models import DoctorProfile , Schedule
# Create your models here.
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]    
    patient=models.ForeignKey(PatientProfile , on_delete=models.CASCADE , related_name='appointment')
    doctor=models.ForeignKey(DoctorProfile , on_delete=models.CASCADE , related_name='appointment')
    schedule=models.ForeignKey(Schedule , on_delete=models.CASCADE , related_name='appointment')
    appointment_date=models.DateTimeField()
    status = models.CharField( max_length=20,choices=STATUS_CHOICES,default='pending')
    reason = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient} - {self.doctor} ({self.appointment_date})"