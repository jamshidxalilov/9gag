from django.urls import path
from .views import RegistrationView, ClientLogin, ClientLogout, ClientProfile


app_name = 'client'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', ClientLogin.as_view(), name='login'),
    path('logout/', ClientLogout.as_view(), name='logout'),
    path('profile/', ClientProfile.as_view(), name='profile')
]
