from rest_framework.routers import DefaultRouter
from django.urls import path , include
from . import views
router=DefaultRouter()
router.register('doctor' , views.DoctorViewSet)
router.register('schedule' , views.ScheduleModelViewSet)
urlpatterns = [
    path('' , include(router.urls))
]


#           python manage.py runserver