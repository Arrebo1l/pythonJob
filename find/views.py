from django.shortcuts import render
from .models import JobPost
from .models import Management
from .models import Sales
from .models import Other


def Coach_Job(request):
    Job = JobPost.objects.all()
    context = {'Job': Job}
    return render(request, 'Finding/JobPost.html', context)


def Coach_Job_detail(request, id):
    Job = JobPost.objects.get(id=id)
    context = {'Job': Job}
    return render(request, 'Finding/detail.html', context)


def Management_Job(request):
    ManagementJob = Management.objects.all()
    context = {'Management_Job': ManagementJob}
    return render(request, 'Finding/Management.html', context)


def Management_Job_detail(request, id):
    ManagementJob = Management.objects.get(id=id)
    context = {'Management_Job': ManagementJob}
    return render(request, 'Finding/Management_detail.html', context)


def Sales_Job(request):
    SalesJob = Sales.objects.all()
    context = {'Sales_Job': SalesJob}
    return render(request, 'Finding/Sales.html', context)


def Sales_Job_detail(request, id):
    SalesJob = Sales.objects.get(id=id)
    context = {'Sales_Job': SalesJob}
    return render(request, 'Finding/Sales_detail.html', context)


def Other_Job(request):
    OtherJob = Other.objects.all()
    context = {'Other_Job': OtherJob}
    return render(request, 'Finding/Other.html', context)


def Other_Job_detail(request, id):
    OtherJob = Other.objects.get(id=id)
    context = {'Other_Job': OtherJob}
    return render(request, 'Finding/Other_detail.html', context)

