from rest_framework.routers import DefaultRouter
from django.urls import path , include
from . import views
router=DefaultRouter()
router.register('invoice' , views.InviceModelViewSet)

urlpatterns = [
    path('' , include(router.urls)),
    path('payment/' , views.PaymentAPIView.as_view() , name="payment"),
    path('payment/<int:pk>/' , views.PaymentDetailAPIView.as_view() , name="payment-detail")
]