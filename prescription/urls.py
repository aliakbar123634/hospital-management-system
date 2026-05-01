from rest_framework.routers import DefaultRouter
from django.urls import path , include
from . import views
router=DefaultRouter()
router.register('prescription' , views.PrescriptionViewSet)
router.register('medicalrepost' , views.MedicalReportViewSet)
urlpatterns = [
    path('' , include(router.urls))
]