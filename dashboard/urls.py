from django.urls import path
from dashboard import views

urlpatterns = [
    path('orders', views.recent_orders, name=('orders')),
]
