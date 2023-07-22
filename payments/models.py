from django.db import models


class PaymentMethod(models.Model):
    method_type = models.CharField(max_length=50)
    Card_number = models.CharField(max_length=50)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=5)


class Transaction(models.Model):
    payment_method = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
