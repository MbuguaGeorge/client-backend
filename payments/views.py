from tabnanny import check
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import views
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
import json
import io

from checkout_sdk.checkout_sdk import CheckoutSdk
from checkout_sdk.environment import Environment
from checkout_sdk.payments.payments import PaymentRequestCardSource, PaymentRequest, CustomerRequest
from checkout_sdk.exception import CheckoutApiException, CheckoutArgumentException, CheckoutAuthorizationException
from checkout_sdk.common.enums import Currency
import requests

# Create your views here.
class CardDetailsView(views.APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.method == 'POST':
                json_data = request.body
                stream = io.BytesIO(json_data)
                st_data = JSONParser().parse(stream)
                card_no = st_data.get('card_no', None)
                card_cvv = st_data.get('card_cvv', None)
                expiry = st_data.get('expiry', None)
                amount = st_data.get('amount', None)
                name = st_data.get('name', None)
                email = st_data.get('email', None)

                if card_no is not None and card_cvv is not None and expiry is not None and amount is not None and name is not None and email is not None:
                    month = expiry[:2]
                    year = expiry[-4:]
                    credentials = {
                        "card_no": card_no,
                        "card_cvv": card_cvv,
                        "month": month,
                        "year": year,
                        "amount": amount,
                        "name": name,
                        "email": email
                    }

                    return Response(credentials)

                else:
                    return Response({'Error': 'Invalid data'})

@api_view(['GET',])
@permission_classes((permissions.AllowAny,))
def receive_payment(request):
    api = CheckoutSdk.builder().secret_key('sk_sbox_swezsqazkhbmskkhm2vawdjt7yc').environment(Environment.sandbox()).build()
    
    request_card_source = PaymentRequestCardSource()
    request_card_source.type = 'card'
    request_card_source.number = '4543474002249996'
    request_card_source.expiry_month = 6
    request_card_source.expiry_year = 2025
    request_card_source.cvv = '956'

    customer_request = CustomerRequest()
    customer_request.email = 'mbuguag026@gmail.com'
    customer_request.name = 'George Mbugua'

    request = PaymentRequest()
    request.source = request_card_source
    request.currency = 'USD'
    request.amount = 200
    request.capture = False
    request.reference = '#123'
    request.customer = customer_request
    request.processing_channel_id = "pc_vweppgh5z4befjkufgnowprvm4"

    try:
        response = api.payments.request_payment(request)
        return Response({'success': 'Payment sent Successfully'})
    except CheckoutApiException:
        return Response({
            'Failed': 'Payment was not a success',
        })