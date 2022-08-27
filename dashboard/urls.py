from django.urls import path
from dashboard import views

urlpatterns = [
    path('orders', views.recent_orders, name=('orders')),
    path('list', views.Order.as_view()),
]
