from django.shortcuts import render
from django.http import HttpResponse
from .models import EducationPost


def education(request):
    educations = EducationPost.objects.all()
    context = {'educations': educations}
    return render(request, 'Rehabilitation/education.html', context)