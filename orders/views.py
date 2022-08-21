from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from orders.serializers import SummarySerializer, DetailSerializer, RequirementSerializer

# Create your views here.
@permission_classes((IsAuthenticated,))
class SummaryList(APIView):
    def post(self, request):
        detail_serializer = DetailSerializer(data=request.data)
        summary_serializer = SummarySerializer(data=request.data)
        requirement_serializer = RequirementSerializer(data=request.data)

        data = {}
        data1 = {}
        data2 = {}

        if detail_serializer.is_valid():
            detail = detail_serializer.save()
            data1['paper_type'] = detail.paper_type
            data1['subject'] = detail.subject
            data1['pages'] = detail.pages
        else:
            data1 = detail_serializer.errors

        if requirement_serializer.is_valid():
            requirement = requirement_serializer.save()
            data2['instructions'] = requirement.instructions
            data2['instruction_file'] = requirement.instruction_file
            data2['paper_format'] = requirement.paper_format
            data2['references'] = requirement.references
        else:
            data2 = requirement_serializer.errors

        if summary_serializer.is_valid():
            summary = summary_serializer.save()
            summary.user = request.user
            summary.save()
            data['order_type'] = summary.order_type
            data['academic_year'] = summary.academic_year
            data['deadline'] = summary.deadline
            data['paper_level'] = summary.paper_level
            data['upgrade'] = summary.upgrade
        else:
            data = summary_serializer.errors

        return Response(data)