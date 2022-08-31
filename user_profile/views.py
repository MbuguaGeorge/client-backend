from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from django.conf import settings
import json
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

from user_profile.serializers import ProfileSerializer
from user_profile.models import User

# Create your views here.
@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def register(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False
            user.save()
            data['response'] = 'success'
            data['email'] = user.email
            data['name'] = user.name
            data['phone'] = user.phone

            confirmation_Token = user.email_token
            activate_link_url = 'http://127.0.0.1:3000' + '/email-verified/' + confirmation_Token

            subject='EMAIL CONFIRMATION'
            html_content=render_to_string('user_profile/email.html', {'verify_link': activate_link_url})
            text_content=strip_tags(html_content)
            email_from=settings.EMAIL_HOST_USER
            recepient_list=[data['email']]

            msg=EmailMultiAlternatives(subject,text_content,email_from,recepient_list)
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return Response({"success":"an email confirmation link was sent to you"})

        else:
            data = serializer.errors
            return Response({'Invalid': data})


@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def validate(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        verify_token = data['email_token']
        res = {
            'status': 'success',
            'message': 'Valid',
        }
            
        if User.objects.filter(email_token=verify_token).exists():
            tokenExists = User.objects.get(email_token=verify_token)

            tokenExists.is_active = True
            tokenExists.save()

        else:
            res = {
                'status': 'failed',
                'message': 'Invalid',
            }
                
        return Response(res) 

@permission_classes((permissions.AllowAny,))
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)
        serializer = ProfileSerializer(user)

        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({"token": user.auth_token.key, "user": serializer.data})
        else:
            return Response({"error": "Wrong credentials"}, status = status.HTTP_400_BAD_REQUEST)