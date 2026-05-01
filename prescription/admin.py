from django.contrib import admin
from . models import Prescription , MedicalReport
# Register your models here.
admin.site.register(Prescription)
admin.site.register(MedicalReport)



#                  python manage.py runserver