from django.db import models
from appointments.models import Appointment
from patients.models import PatientProfile
class Prescription(models.Model):
    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name="prescription"
    )
    diagnosis = models.TextField()
    medicines = models.TextField()
    dosage = models.TextField()
    instructions = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Prescription for {self.appointment}"
    

class MedicalReport(models.Model):
    REPORT_TYPES = [
        ('blood', 'Blood Test'),
        ('xray', 'X-Ray'),
        ('mri', 'MRI'),
        ('ct', 'CT Scan'),
        ('other', 'Other'),
    ]

    patient = models.ForeignKey(
        PatientProfile,
        on_delete=models.CASCADE,
        related_name="reports"
    )

    prescription = models.ForeignKey(
        Prescription,
        on_delete=models.CASCADE,
        related_name="reports"
    )

    report_type = models.CharField(
        max_length=20,
        choices=REPORT_TYPES
    )

    report_file = models.FileField(
        upload_to="reports/"
    )

    remarks = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient} - {self.report_type}"    