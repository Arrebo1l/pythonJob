from django.urls import path
from . import views

app_name = 'Online'

urlpatterns = [
    path('Online_Consultation/', views.Online_Consultation, name='Online_Consultation'),
    path('Online_Consultation-detail/<int:id>/', views.Doctors_detail, name='Online_Consultation-detail'),
]
