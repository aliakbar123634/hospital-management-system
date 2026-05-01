from rest_framework.routers import DefaultRouter
from django.urls import path , include
from . import views
router=DefaultRouter()
router.register('patients' , views.PatientModelViewSet)
router.register('medicalhistory' , views.MedicalHistoryViewSet)
urlpatterns = [
    path('' , include(router.urls))
]


#           python manage.py runserver