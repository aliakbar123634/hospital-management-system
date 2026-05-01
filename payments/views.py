from django.shortcuts import render
# from pytz import timezone
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from . permission import AdminRecipentAllDoctorPatientOwn , AdminResipent , BlockUpdateDeletePermission, DoctorPatient , AdminRecipentallPatientOwn
from rest_framework.decorators import action 
from django.db import transaction
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.shortcuts import get_object_or_404
# Create your views here............
class InviceModelViewSet(ModelViewSet):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer
    permission_classes=[AdminRecipentAllDoctorPatientOwn]
    def get_permissions(self):
        if self.action=="create":
            return [AdminResipent()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [BlockUpdateDeletePermission()]
        return super().get_permissions()
    @action(detail=True , methods=['GET'] , url_path="download" , permission_classes=[AdminRecipentAllDoctorPatientOwn])
    def downloadpdf(self , request , pk=None):
        invoice = self.get_object()
    # response create (PDF)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="invoice_{invoice.id}.pdf"'
    # PDF document
        doc = SimpleDocTemplate(response)
        styles = getSampleStyleSheet()
        elements = []
    # Content
        elements.append(Paragraph(f"Invoice ID: {invoice.id}", styles['Title']))
        elements.append(Spacer(1, 10))
        elements.append(Paragraph(f"Patient: {invoice.appointment.patient}", styles['Normal']))
        elements.append(Paragraph(f"Doctor: {invoice.appointment.doctor}", styles['Normal']))
        elements.append(Spacer(1, 10))
        elements.append(Paragraph(f"Amount: {invoice.total_amount}", styles['Normal']))
        elements.append(Paragraph(f"Status: {invoice.status}", styles['Normal']))
        elements.append(Spacer(1, 10))
        elements.append(Paragraph(f"Date: {invoice.created_at}", styles['Normal']))
    # build PDF
        doc.build(elements)
        return response
    
class PaymentAPIView(APIView):
    permission_classes=[DoctorPatient]
    def post(self , request):
        invoice_id=request.data.get('invoice')
        try:
            invoice=Invoice.objects.get(id=invoice_id)
        except Invoice.DoesNotExist:
            return Response({
            "message":"Please Enter correct Invoice ..........."
        }, status=status.HTTP_400_BAD_REQUEST)    
        if invoice.status=="paid": 
            return Response({
                "message":"Invoice already paid ............"
            },status=status.HTTP_400_BAD_REQUEST)
        invoice_amount=float(request.data.get('amount'))
        if invoice.final_amount<invoice_amount:  
            return Response({
                "message":"You have entered more amount than required............"
            },status=status.HTTP_400_BAD_REQUEST)  
        if invoice.final_amount>invoice_amount:  
            return Response({
                "message":"Your amount is less than the required amount ............"
            },status=status.HTTP_400_BAD_REQUEST) 
        transaction_id=request.data.get("transaction_id") 
        payment_method=request.data.get("payment_method")                       
        with transaction.atomic():    
            payment=Payment.objects.create(
                invoice=invoice,
                payment_method=payment_method,
                transaction_id=transaction_id,
                amount=invoice_amount,
                payment_status="success",
                paid_at=timezone.now()
            )
            invoice.status="paid"
            invoice.save()
        return Response({
                "id":payment.id, 
                "invoice" : invoice.id,
                "payment_method": payment_method,
                "transaction_id": transaction_id,
                "amount":invoice_amount,
                "payment_status":"success",
                "paid_at": payment.paid_at,
                "created_at": payment.created_at,
                "updated_at": payment.updated_at        
        }, status =status.HTTP_200_OK)    



class PaymentDetailAPIView(APIView):
    permission_classes=[AdminRecipentallPatientOwn]    
    def get_obj(self , pk):
        return get_object_or_404(Payment, id=pk)
       
    def get(self , request , pk):
        pay=self.get_obj(pk)
        self.check_object_permissions(request, pay)
        serializer=PaymentSerializer(pay)
        return Response(serializer.data ,status=status.HTTP_200_OK )










    



#                  python manage.py runserver    