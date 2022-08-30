from dashboard.serializers import OrderSerialzer, ListOrdersSerializer
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
import io
from rest_framework.parsers import JSONParser

from orders.models import Academic_Writing
from dashboard.models import Recent_Orders

# Create your views here.
@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def updatestatus(request, pk):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            json_data = request.body
            stream = io.BytesIO(json_data)
            st_data = JSONParser().parse(stream)
            status = st_data.get('status', None)
            if status is not None:
                order = Recent_Orders.objects.get(id=pk)
                serializer = OrderSerialzer(order, data=st_data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': 'status successfully updated'})
                return Response({'message': 'data not valid'})

class OrderView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get(self, request, pk):
        res = []
        order = Recent_Orders.objects.get(id=pk)
        serializer = ListOrdersSerializer(order)
        data = serializer.data
        res.append(data)
        return Response(res)

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

class Newly_Created_Order(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get(self, request, pk):
        order = Recent_Orders.objects.get(details__id=pk)
        serializer = ListOrdersSerializer(order)
        return Response(serializer.data)