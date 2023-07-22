from rest_framework import serializers

from .models import PaymentMethod, Transaction


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['id', 'method_type', 'Card_number', 'expiration_date', 'cvv']


class TransactionSerializer(serializers.ModelSerializer):
    payment_method = PaymentMethodSerializer()

    class Meta:
        model = Transaction
        fields = ['id', 'payment_method', 'amount', 'date', 'status']
