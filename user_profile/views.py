from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status, generics
from rest_framework.decorators import api_view, permission_classes
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
import json
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

from user_profile.serializers import ProfileSerializer, UsersSerializer, ProfileUpdateSerializer
from user_profile.models import User

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created

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
            # create a link that contains a token to validate a user email
            activate_link_url = 'https://georgeclientapp.netlify.app' + '/verified/' + confirmation_Token

            # send a mail with the email validation link
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
            
        if User.objects.filter(email_token=verify_token).exists(): # Verify if the received token checks with the one stored 
                                                                    # for that partifcular user
            tokenExists = User.objects.get(email_token=verify_token)

            tokenExists.is_active = True 
            tokenExists.save()

        else:
            res = {
                'status': 'failed',
                'message': 'Invalid',
            }
                
        return Response(res) 

# Authenticate a user
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

# Gets current user
class CurUser(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get(self, request):
        res = []
        serializer = ProfileSerializer(request.user)
        res.append(serializer.data)
        return Response(res)

class UpdateUser(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, format=None):
        res = []
        serializer = ProfileUpdateSerializer(request.user, data=request.data, partial=True)
        data = {}
        if serializer.is_valid():
            serializer.save()
            res.append(serializer.data)
            data['success'] = "updated successfully"
            return Response(res)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# pull all users
class ListUsers(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    serializer_class = UsersSerializer

    def get_queryset(self):
        return User.objects.all()

# Password reset
@receiver(reset_password_token_created)
@permission_classes((permissions.AllowAny,))
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    user_email = reset_password_token.user.email
    reset_url = "https://georgeclientapp.netlify.app/password-change/" + reset_password_token.key

    subject='FORGOT PASSWORD'
    html_content=render_to_string('user_profile/password-reset.html', {'reset_url': reset_url})
    text_content=strip_tags(html_content)
    email_from=settings.EMAIL_HOST_USER
    recepient_list=[user_email,]

    msg=EmailMultiAlternatives(subject,text_content,email_from,recepient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return Response({'success': 'email changed successfully'})