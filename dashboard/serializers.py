from rest_framework import serializers
from dashboard.models import Recent_Orders
from orders.serializers import SummarySerializer

class OrderSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Recent_Orders
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

class AmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recent_Orders
        fieds = ('amount',)
        
    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.save()
        return instance

class ListOrdersSerializer(serializers.ModelSerializer):
    details = SummarySerializer(read_only=True)
    class Meta:
        model = Recent_Orders
        fields = ('id', 'details', 'status')