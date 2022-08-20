from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

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
            user.is_active = False
            user.save()
            data['response'] = 'success'
            data['email'] = user.email
            data['name'] = user.name
            data['phone'] = user.phone

            confirmation_Token = default_token_generator.make_token(user)
            activate_link_url = 'http://127.0.0.1:3000' + '/verify/' + confirmation_Token

            subject='EMAIL CONFIRMATION'
            html_content=render_to_string('user_profile/email.html', {'verify_link': activate_link_url})
            text_content=strip_tags(html_content)
            email_from=settings.EMAIL_HOST_USER
            recepient_list=[data['email']]

            msg=EmailMultiAlternatives(subject,text_content,email_from,recepient_list)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            #send_mail(subject,message,email_from,recepient_list)

        else:
            data = serializer.errors

        return Response("Check your email for a confirmation link")

# @api_view(['GET',])
# @permission_classes((permissions.AllowAny,))
# def activate(self, request, pk=None):
#     data = json.loads(request.body.decode('utf-8'))
#     token = data['token']
#     res = {
#         'status': 'success',
#         'message': 'Valid',
#     }
    
#     if GeneralUser.objects.filter(email_verified_hash=token, email_verified=0).exists():
#         tokenExists = GeneralUser.objects.get(email_verified_hash=token, email_verified=0)

#         tokenExists.email_verified = 1
#         tokenExists.save()

#     else:
#         res = {
#             'status': 'failed',
#             'message': 'Invalid',
#         }
    
#     return JsonResponse(res) 