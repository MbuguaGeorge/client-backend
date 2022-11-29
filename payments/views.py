from rest_framework.response import Response
from rest_framework import views
from dashboard.models import Recent_Orders
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.conf import settings
import io

from checkout_sdk.checkout_sdk import CheckoutSdk
from checkout_sdk.environment import Environment
from checkout_sdk.payments.payments import PaymentRequestCardSource, PaymentRequest, CustomerRequest
from checkout_sdk.exception import CheckoutApiException
from checkout_sdk.common.enums import Currency

# Create your views here.
class PaymentProcessView(views.APIView):
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
                ref = st_data.get('ref', None)

                if card_no is not None and card_cvv is not None and expiry is not None and amount is not None and name is not None and email is not None:
                    month = expiry[:2] # Get the first two characters
                    year = expiry[-4:] # Get the last four characters
                    total_amount = float(amount)
                    pk = int(ref)

                    api = CheckoutSdk.builder().secret_key(settings.CHECKOUT_API_KEY).environment(Environment.sandbox()).build()
                    
                    # Card details
                    request_card_source = PaymentRequestCardSource()
                    request_card_source.type = 'card'
                    request_card_source.number = card_no
                    request_card_source.expiry_month = int(month)
                    request_card_source.expiry_year = int(year)
                    request_card_source.cvv = card_cvv

                    # Customer details
                    customer_request = CustomerRequest()
                    customer_request.email = email
                    customer_request.name = name

                    # Payment details
                    request = PaymentRequest()
                    request.source = request_card_source
                    request.currency = Currency.USD
                    request.amount = total_amount
                    request.capture = False
                    request.reference = ref
                    request.customer = customer_request
                    request.processing_channel_id = settings.CHECKOUT_CHANNEL_ID

                    try:
                        response = api.payments.request_payment(request)
                        order = Recent_Orders.objects.get(id=pk) # Set order payment complete
                        order.complete = True 
                        order.save()
                        return Response({
                            'status': 'success',
                            'message' : 'Payment sent Successfully',
                            'response': response
                        })
                    except CheckoutApiException:
                        return Response({
                            'status': 'failed',
                            'message' : 'Invalid card details'
                        })