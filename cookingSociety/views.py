from django.shortcuts import render, get_object_or_404
from .models import Cooker
from .models import Dish
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def index(request):
    cookerlist = Cooker.objects.all()
    dishlist = Dish.objects.all()
    context = {'cookerlist': cookerlist, 'dishlist': dishlist}
    return render(request, 'cookingSociety/index.html', context)

def cooker_detail(request, cooker_id):
    cooker = get_object_or_404(Cooker, pk=cooker_id)
    dishlist = Dish.objects.all()
    superdishlist = []
    for dish in dishlist:
        if cooker.ableCookSupper(dish):
            superdishlist.append(dish)
    context = {'cooker': cooker, 'supdishlist': superdishlist}
    return render(request, 'cookingSociety/details.html', context)

def cooker_create(request):
    return render(request, 'cookingSociety/cookercreate.html')

@csrf_protect
def cooker_new(request):
    args = request.POST # dict
    cooker = Cooker()
    if 'name' in args:
        cooker.name = args['name']
    else:
        cooker.name = "XiaoWang8"
    if 'skill1' in args:
        cooker.skill1 = int(args['skiil1'])
    if 'skill2' in args:
        cooker.skill2 = int(args['skiil2'])
    if 'skill3' in args:
        cooker.skill3 = int(args['skiil3'])
    if 'skill4' in args:
        cooker.skill4 = int(args['skiil4'])
    if 'skill5' in args:
        cooker.skill5 = int(args['skiil5'])
    if 'skill6' in args:
        cooker.skill6 = int(args['skiil6'])
    cooker.save()
    cookerlist = Cooker.objects.all()
    dishlist = Dish.objects.all()
    context = {'cookerlist': cookerlist, 'dishlist': dishlist}
    return render(request, 'cookingSociety/index.html', context)
