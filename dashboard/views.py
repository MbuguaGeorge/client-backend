from dashboard.serializers import OrderSerialzer
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated

from orders.models import Academic_Writing

# Create your views here.
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def recent_orders(request):
    if request.method == 'POST':
        order_details = Academic_Writing.objects.get(user=request.user)
        serializer = OrderSerialzer(data=request.data)
        data = {}

        if serializer.is_valid():
            order = serializer.save()
            order.details = order_details
            order.user = request.user
            order.save()
            data['response'] = 'success'
            data['status'] = order.status
        else:
            data = serializer.errors
        return Response(data)