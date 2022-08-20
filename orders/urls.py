from django.urls import path
from orders import views


urlpatterns = [
    path('summary', views.SummaryList.as_view()),
]
