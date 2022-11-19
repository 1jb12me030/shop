from django.urls import path
from .views import *
urlpatterns = [
    path('register/',RegistrationView.as_view()),
    path('login/',LoginView.as_view()),
    path('logout/',LogOutView.as_view()),
    path('location/',RegisterLocationView.as_view()),
    path('shop/',ShopView.as_view()),
    

]