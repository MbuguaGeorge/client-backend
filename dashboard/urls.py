from django.urls import path
from dashboard import views

urlpatterns = [
    path('status/<int:pk>', views.updatestatus, name=('status')),
    path('list', views.Order.as_view()),
    path('recent/<int:pk>', views.OrderView.as_view()),
]
