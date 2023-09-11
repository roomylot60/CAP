from django.urls import path
from Common_Alerting_Protocol import views

app_name = 'Common_Alerting_Protocol'

urlpatterns = [
    path('', views.header), 
    path('create/', views.create), 
    path('message/', views.message), 
    path('area/', views.area),
]
