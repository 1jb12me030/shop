from django.urls import path
from .views import *

from testapp import views
urlpatterns = [
    path('register/',RegistrationView.as_view()),
    path('login/',LoginView.as_view()),
    path('logout/',LogOutView.as_view()),
    path('location/',RegisterLocationView.as_view()),
    path('shop/',ShopView.as_view()),
    path('test/all/', views.index1_view),
    path('test/', views.index_view),
    

]