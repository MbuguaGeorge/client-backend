from django.urls import path
from user_profile import views

urlpatterns = [
    path('register', views.register, name=('register')),
    path('validate', views.validate, name=('validate')),
]
