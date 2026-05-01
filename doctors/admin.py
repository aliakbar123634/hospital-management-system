from django.contrib import admin
from . models import DoctorProfile , Schedule
# Register your models here.
admin.site.register(DoctorProfile)
admin.site.register(Schedule)


#            python manage.py runserver