from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(PatientProfile)
admin.site.register(MedicalHistory)


#            python manage.py runserver