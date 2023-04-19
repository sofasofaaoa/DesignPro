from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('requests', RequestListView.as_view(), name='requests'),
    path('request/create', CreateRequest.as_view(), name='create-request'),
    path(r'^request/(?P<pk>\w+)/(?P<st>\w+)/update/$', confirm_update, name='update-request'),
    path('request/<pk>/delete', DeleteRequest.as_view(), name='delete-request'),
    path('categories', CategoryListView.as_view(), name='categories'),
    path('category/create', CreateCategory.as_view(), name='create-cat'),
    path('category/<pk>/delete', DeleteCategory.as_view(), name='delete-cat'),
    path('accounts/login', BBLoginView.as_view(), name='login'),
    path('accounts/logout', BBLogoutView.as_view(), name='logout'),
    path('accounts/register', RegisterView.as_view(), name='register'),
]
