from django.urls import path
from . import views

app_name = 'find'

urlpatterns = [
    path('Coach-Job/', views.Coach_Job, name='Coach_Job'),
    path('Coach-Job-detail/<int:id>/', views.Coach_Job_detail, name='Coach_Job-detail'),
    path('Management-Job/', views.Management_Job, name='Management_Job'),
    path('Management-Job-detail/<int:id>/', views.Management_Job_detail, name='Management_Job-detail'),
    path('Sales-Job/', views.Sales_Job, name='Sales_Job'),
    path('Sales-Job-detail/<int:id>/', views.Sales_Job_detail, name='Sales_Job-detail'),
    path('Other-Job/', views.Other_Job, name='Other_Job'),
    path('Other-Job-detail/<int:id>/', views.Other_Job_detail, name='Other_Job-detail'),
]
