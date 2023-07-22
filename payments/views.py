from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from .models import PaymentMethod, Transaction
from .serializers import PaymentMethodSerializer, TransactionSerializer
import datetime

class PaymentMethodViewSet(ViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

    def list(self, request):
        qs = self.queryset
        return Response(self.serializer_class(qs, many=True).data)

    def retrieve(self, request, pm_id):
        pm = self.get_object(pm_id)
        return Response(self.serializer_class(pm).data)

    def create(self, request, pm_id):
        pm = self.get_object(pm_id)
        data = request.data
        transaction = Transaction.objects.create(
            payment_method=pm,
            amount=data["amount"],
            date=datetime.datetime.utcnow()
        )
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], renderer_classes=[TemplateHTMLRenderer])
    def retrieve_transaction(self, request, pm_id, tx_id):
        transaction = Transaction.objects.get(pm_id=pm_id, id=tx_id)
        serializer = TransactionSerializer(transaction)
        return Response({'transaction': serializer.data}, template_name='transaction_detail.html')

    @retrieve_transaction.mapping.post
    def create_transaction(self, request, pm_id, tx_id):
        pm = self.get_object(pm_id)
        data = request.data
        transaction = Transaction.objects.create(
            payment_method=pm,
            amount=data["amount"],
            date=datetime.datetime.utcnow()
        )
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)
