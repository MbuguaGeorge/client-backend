from django.urls import path
from user_profile import views

urlpatterns = [
    path('register', views.register, name=('register')),
    path('validate', views.validate, name=('validate')),
    path('login', views.LoginView.as_view()),
    path('cur', views.CurUser.as_view()),
    path('update', views.UpdateUser.as_view()),
    path('users', views.ListUsers.as_view()),
]
