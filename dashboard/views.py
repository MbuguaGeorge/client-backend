from dashboard.serializers import OrderSerialzer, ListOrdersSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated

from orders.models import Academic_Writing
from dashboard.models import Recent_Orders
from orders.serializers import SummarySerializer

# Create your views here.
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def recent_orders(request):
    if request.user.is_authenticated:
        cur_user = request.user
        if request.method == 'POST':
            order_details = Academic_Writing.objects.get(user=request.user)
            serializer = OrderSerialzer(data=request.data)
            data = {}

            if serializer.is_valid():
                order = serializer.save()
                order.details = order_details
                order.details = Academic_Writing.objects.filter(user=cur_user)
                order.save()
                data['response'] = 'success'
                data['status'] = order.status
            else:
                data = serializer.errors
            return Response(data)

class Order(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get(self, request):
        res = []
        summary = Academic_Writing.objects.filter(user=request.user)
        recent_orders = Recent_Orders.objects.filter(details__user=request.user)
        for order in recent_orders:
            serializer = ListOrdersSerializer(order)
            res.append(serializer.data)
        return Response(res)