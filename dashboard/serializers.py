from rest_framework import serializers
from dashboard.models import Recent_Orders
from orders.serializers import SummarySerializer

class OrderSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Recent_Orders
        fields = ('details', 'status')

    def save(self):
        order = Recent_Orders(
            status = self.validated_data['status']
        )

        order.save()
        return order

class ListOrdersSerializer(serializers.ModelSerializer):
    details = SummarySerializer(read_only=True)
    class Meta:
        model = Recent_Orders
        fields = ('details', 'status')