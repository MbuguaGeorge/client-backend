from django.urls import path
from payments import views

urlpatterns = [
    path('verify', views.CardDetailsView.as_view()),
    path('pay', views.receive_payment, name=('pay')),
]
