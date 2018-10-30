from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Developer, Project

# Create your views here.

def index(request):
    dev_list = Developer.objects.order_by('dev_id')
    proj_list = Project.objects.order_by('proj_stars')
    for proj in proj_list:
        dev = get_object_or_404(Developer, dev_id=proj.proj_owner)
        proj.projowername = dev.dev_name
    for dev in dev_list:
        try:
            dev.ownproj = get_object_or_404(Project, proj_owner=dev.dev_id)
        except:
            dev.ownproj = -1
    context = {'dev_list': dev_list, 'proj_list':proj_list}
    return render(request, 'devprofs/index.html', context)

def developer(request,dev_id):
    dev = get_object_or_404(Developer, dev_id=dev_id)
    inprojs = Project.objects.filter(proj_owner=dev_id) # ! need to change to cp table
    ownprojs = Project.objects.filter(proj_owner=dev_id)
    return render(request, 'devprofs/developer.html', {'dev':dev, 'inprojs':inprojs, 'ownprojs':ownprojs})


def project(request, proj_id):
    proj = get_object_or_404(Project, proj_id=proj_id)
    owner = get_object_or_404(Developer, dev_id=proj.proj_owner)
    return render(request, 'devprofs/project.html', {'proj':proj, 'owner':owner})

