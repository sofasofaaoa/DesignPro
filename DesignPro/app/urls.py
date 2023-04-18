from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login', BBLoginView.as_view(), name='login'),
    path('accounts/logout', BBLogoutView.as_view(), name='logout'),
    path('accounts/register', RegisterView.as_view(), name='register'),
]