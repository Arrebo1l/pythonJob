from django.shortcuts import render
from django.http import HttpResponse

from .forms import OnlineDoctorForm
from .models import OnlineDoctor


def Online_Consultation(request):
    doctors = OnlineDoctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'Rehabilitation/Online_Consultation.html', context)


def Doctors_detail(request, id):
    # 取出相应的文章
    doctor = OnlineDoctor.objects.get(id=id)
    # 需要传递给模板的对象
    context = {'doctors': doctor}
    # 载入模板，并返回context对象
    return render(request, 'Rehabilitation/detail.html', context)


def Doctors_create(request):
    if request.method == "POST":
        # 增加 request.FILES
        Online_Doctor_form = OnlineDoctorForm(request.POST, request.FILES)
