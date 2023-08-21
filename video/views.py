from django.shortcuts import render
from django.http import HttpResponse

from .forms import VideosForm
from .models import VideoList


def VideoView(request):
    video = VideoList.objects.all()
    context = {'videos': video}
    return render(request, 'video/video.html', context)



