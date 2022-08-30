from django.urls import path
from payments import views

urlpatterns = [
    path('receive-payment', views.PaymentProcessView.as_view()),
]
