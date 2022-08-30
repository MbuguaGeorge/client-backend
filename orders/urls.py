from django.urls import path
from orders import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('summary', views.CreateOrderList.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)