from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.login_user, name='login_user'),
    path('sign_up', views.register_user, name='sign_up'),
]



