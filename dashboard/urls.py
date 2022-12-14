from django.urls import path
from dashboard import views

urlpatterns = [
    path('status/<int:pk>', views.updatestatus, name=('status')),
    path('recent/<int:pk>', views.OrderView.as_view()),

    path('list', views.RecentOrder.as_view()),
    path('canceled/', views.CanceledOrder.as_view()),
    path('finished', views.FinishedOrder.as_view()),
    path('revised', views.RevisedOrder.as_view()),

    path('neworder/<str:pk>', views.NewOrder.as_view()),
    path('recentorder/<str:pk>', views.RecentOrderView.as_view()),
]
