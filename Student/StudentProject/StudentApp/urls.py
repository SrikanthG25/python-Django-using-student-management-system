from django.urls import path
from .views import StudentRegister ,LoginView

urlpatterns = [
    path('',StudentRegister.as_view() , name = 'Register'),
    path('<int:pk>/',StudentRegister.as_view() , name = 'Getdata'),
    path('login/',LoginView.as_view() , name = 'Login'),
]