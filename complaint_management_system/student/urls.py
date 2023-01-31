from django.urls import path
from .views import RegisterUserView, LoginUserView

urlpatterns = [
    path('',RegisterUserView.as_view(), name= 'register-user'),
    path('login/', LoginUserView.as_view(), name='login')
]