from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

from user_profile.serializers import ProfileSerializer

# Create your views here.
@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def register(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'success'
            data['email'] = user.email
            data['name'] = user.name
            data['phone'] = user.phone
        else:
            data = serializer.errors
        return Response(data)