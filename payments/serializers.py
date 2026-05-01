from rest_framework import serializers
from . models import Invoice , Payment

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Invoice
        fields=["id","appointment","total_amount","discount","tax","final_amount","status","issued_date","created_at","updated_at"]
        read_only_fields=["id","created_at","updated_at"]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields=["id","invoice","payment_method","transaction_id","amount","payment_status","paid_at","created_at","updated_at"]
        read_only_fields=["id","created_at","updated_at"]
