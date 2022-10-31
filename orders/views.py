from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from orders.serializers import SummarySerializer
from rest_framework.views import APIView

# Create your views here.
class CreateOrderList(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
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
                    data['programming_category'] = order.programming_category
                    data['prog_language'] = order.prog_language
                    data['task_size'] = order.task_size
                    data['amount'] = order.amount
                    data['discipline'] = order.discipline
                    data['software'] = order.software
                    data['spacing'] = order.spacing

                    serializer1 = SummarySerializer(order)
                    return Response(serializer1.data)

                else:
                    data = serializer.errors
                    return Response({'Invalid': data})