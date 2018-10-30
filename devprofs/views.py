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

    ca_Classlist = [
        'Documentation', 'CodeStyle', 'Performance', 'JavaPractices', 'Security', 'Multithreading', 'Design', 'ErrorProne'
    ]
    ca_Scorelist = [
        dev.dev_score_Documentation,
        dev.dev_score_CodeStyle,
        dev.dev_score_Performance,
        dev.dev_score_BestPractices,
        dev.dev_score_Security,
        dev.dev_score_Multithreading,
        dev.dev_score_Design,
        dev.dev_score_ErrorProne
    ]
    ca_Averagelist = [60,60,60,60,60,60,60,60] # need data
    ca_indicator = '['
    for caclass in ca_Classlist:
        ca_indicator += "{name: '"+caclass+"', max: 100},"
    ca_indicator += ']'
    sp_Classlist = [
        'NetWork', 'I/O', 'Math', 'Database','Security',  'Text', 'GUI', 'Others'
    ]
    sp_Scorelist = [
        dev.dev_score_API1,
        dev.dev_score_API2,
        dev.dev_score_API3,
        dev.dev_score_API4,
        dev.dev_score_API5,
        dev.dev_score_API6,
        dev.dev_score_API7,
        dev.dev_score_API8 + dev.dev_score_API9 + dev.dev_score_API10
    ]
    sp_Averagelist = [60, 60, 60, 60, 60, 60, 60, 180]
    sp_indicator = [{'name': spclass, 'max': 100} for spclass in sp_Classlist] # need data
    inProjList = [{'text':proj.proj_name, 'url':'/devprofs/project/' + str(proj.proj_id)} for proj in inprojs]
    ownProjList = [{'text':proj.proj_name, 'url':'/devprofs/project/' + str(proj.proj_id)} for proj in ownprojs]
    calist = [{'Class':ca_Classlist[i], 'caindicator':ca_indicator, 'Score':ca_Scorelist[i]} for i in range(len(ca_Classlist))]
    splist = [{'Class':sp_Classlist[i], 'spindicator':sp_indicator, 'Score':sp_Scorelist[i]} for i in range(len(sp_Classlist))]
    dict_for_html = {
        'devName':dev.dev_name,
        'Githubsite':{
            'text':'https://github.com/' + dev.dev_name,
            'url':'https://github.com/' + dev.dev_name},
        'ActiveIn':inProjList, # [ {'text':'', 'url':''} ]
        'Own':ownProjList, # [ {'text':'', 'url':''} ]
        'CodingAbilities':{'calist':calist, 'ca_Scorelist':ca_Scorelist, 'caAverage':ca_Averagelist},
        'SkillPreference':{'splist':splist, 'sp_Scorelist':sp_Scorelist, 'spAverage':sp_Averagelist}}

    return render(request, 'devprofs/developer.html', {'dict_for_html':dict_for_html})


def project(request, proj_id):
    proj = get_object_or_404(Project, proj_id=proj_id)
    owner = get_object_or_404(Developer, dev_id=proj.proj_owner)
    return render(request, 'devprofs/project.html', {'proj':proj, 'owner':owner})

