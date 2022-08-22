from rest_framework import serializers
from dashboard.models import Recent_Orders

class OrderSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Recent_Orders
        fields = ('user', 'details', 'status')

    def save(self):
        order = Recent_Orders(
            status = self.validated_data['status']
        )

        order.save()
        return order