from django.urls import path
from django.contrib.auth import views as auth_views
from Common_Alerting_Protocol import views

app_name = 'accounts'

urlpatterns = [
    path('log_in/', auth_views.LoginViews.as_view(), name='log_in'), 
    path('log_out/', auth_views.LogoutViews.as_view(), name='log_out'), 
    path('sign_up/', views.sign_up, name='sign_up'), 
]
