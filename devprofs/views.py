from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Developer, Project

# Create your views here.

def index(request):
    dev_list = Developer.objects.order_by('dev_score_All')
    proj_list = Project.objects.order_by('proj_stars')
    context = {'dev_list': dev_list, 'proj_list':proj_list}
    return render(request, 'devprofs/index.html', context)

def developer(request,dev_id):
    dev = get_object_or_404(Developer, dev_id=dev_id)
    return render(request, 'devprofs/developer.html', {'dev':dev})


def project(request, proj_id):
    proj = get_object_or_404(Project, proj_id=proj_id)
    return render(request, 'devprofs/project.html', {'proj':proj})

