from django.shortcuts import render, get_object_or_404
from .models import Cooker
from .models import Dish

# Create your views here.
def index(request):
    cookerlist = Cooker.objects
    dishlist = Dish.objects
    context = {'cookerlist': cookerlist, 'dishlist': dishlist}
    return render(request, 'cookingSociety/index.html', context)

def detail(request, cooker_id):
    cooker = get_object_or_404(Cooker, pk=cooker_id)
    dishlist = Dish.objects
    context = {'cooker': cooker, 'dishlist': dishlist}
    return render(request, 'cookingSociety/details.html', context)