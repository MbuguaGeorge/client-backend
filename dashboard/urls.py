from django.urls import path
from dashboard import views

urlpatterns = [
    path('status/<int:pk>', views.updatestatus, name=('status')),
    path('list', views.RecentOrder.as_view()),
    path('recent/<int:pk>', views.OrderView.as_view()),
    path('canceled/', views.CanceledOrder.as_view()),
]
