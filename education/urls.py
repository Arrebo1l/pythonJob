from django.urls import path
from . import views

app_name = 'education'

urlpatterns = [
     path('education-post/', views.education, name='education-post'),
]
