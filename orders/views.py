from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from orders.serializers import SummarySerializer
from orders.models import Academic_Writing
from dashboard.serializers import OrderSerialzer

# Create your views here.
@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def order(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            serializer = SummarySerializer(data=request.data)
            data = {}

            if serializer.is_valid():
                order = serializer.save()
                order.user = request.user
                order.save()
                data['response'] = 'success'
                data['order_type'] = order.order_type
                data['academic_year'] = order.academic_year
                data['deadline'] = order.deadline
                data['paper_level'] = order.paper_level
                data['title'] = order.title
                data['upgrade'] = order.upgrade
                data['paper_type'] = order.paper_type
                data['subject'] = order.subject
                data['pages'] = order.pages
                data['charts'] = order.charts
                data['slides'] = order.slides
                data['instructions'] = order.instructions
                # data['instruction_file'] = order.instruction_file
                data['paper_format'] = order.paper_format
                data['references'] = order.references

            else:
                data = serializer.errors

            return Response(data)
