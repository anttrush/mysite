from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Developer, Project
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):
    dev_list = Developer.objects.order_by('dev_follower_Number').reverse()
    pageinator = Paginator(dev_list, 25)

    page = request.GET.get('page')
    try:
        devs = pageinator.page(page)
    except PageNotAnInteger:
        devs = pageinator.page(1)
    except EmptyPage:
        devs = pageinator.page(pageinator.num_pages)

    return render(request, 'devprofs/index.html', {'dev_list':devs})
'''
def index(request):
    dev_list = Developer.objects.order_by('dev_follower_Number').reverse()
    proj_list = Project.objects.order_by('proj_stars')
    for proj in proj_list:
        dev = get_object_or_404(Developer, dev_id=proj.proj_owner)
        proj.projowername = dev.dev_name
    for dev in dev_list:
        try:
            dev.ownproj = get_object_or_404(Project, proj_owner=dev.dev_id)
        except:
            dev.ownproj = None
    context = {'dev_list': dev_list, 'proj_list':proj_list}
    return render(request, 'devprofs/index.html', context)
'''

def developer(request,dev_id):
    dev = get_object_or_404(Developer, dev_id=dev_id)
    inprojs = Project.objects.filter(proj_owner=dev_id) # ! need to change to cp table
    ownprojs = Project.objects.filter(proj_owner=dev_id)

    ca_Classlist = [
        'Code Style','Design', 'Documentation','Error Prone', 'Performance', 'Multithreading', 'Security', 'others',
    ]
    ca_Scorelist = [
        round(dev.dev_score_CodeStyle,3),
        round(dev.dev_score_Design,3),
        round(dev.dev_score_Documentation,3),
        round(dev.dev_score_ErrorProne,3),
        round(dev.dev_score_Performance,3),
        round(dev.dev_score_Multithreading,3),
        round(dev.dev_score_Security,3),
        round(dev.dev_score_Others,3)
    ]
    ca_Averagelist = [34.185,32.400,32.273,34.899,40.323,41.222,43.017,36.267] # need data
    ca_indicator = '['
    for caclass in ca_Classlist:
        ca_indicator += "{name: '"+caclass+"', max: 100},"
    ca_indicator += ']'
    sp_Classlist = [
        'Text', 'Graph', 'Math', 'Net', 'IO', 'Database', 'Security', 'Others'
    ]
    sp_Scorelist = [
        round(dev.dev_score_text,3),
        round(dev.dev_score_graph,3),
        round(dev.dev_score_math,3),
        round(dev.dev_score_net,3),
        round(dev.dev_score_IO,3),
        round(dev.dev_score_database,3),
        round(dev.dev_score_secure,3),
        round(dev.dev_score_other,3)
    ]
    sp_Averagelist = [5.393, 1.575, 2.355, 8.459, 15.929, 2.072, 4.397, 34.861]
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
        'SkillPreference':{'splist':splist, 'sp_Scorelist':sp_Scorelist, 'spAverage':sp_Averagelist},
        'effe': round(dev.dev_score_Efficient,2),
        'cLOC': dev.dev_score_cLOC,
        'followerNum': dev.dev_follower_Number
    }

    return render(request, 'devprofs/developer.html', {'dict_for_html':dict_for_html})


def project(request, proj_id):
    proj = get_object_or_404(Project, proj_id=proj_id)
    owner = get_object_or_404(Developer, dev_id=proj.proj_owner)
    return render(request, 'devprofs/project.html', {'proj':proj, 'owner':owner})

