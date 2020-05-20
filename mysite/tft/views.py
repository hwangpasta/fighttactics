from django.http import HttpResponse, request, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Champion



def index(request):
    champion_list = Champion.objects.all()
    template = loader.get_template('tft/index.html')
    context = {'champion_list':champion_list}
    return HttpResponse(template.render(context,request))

def detail(request, champion_id):
    champion = get_object_or_404(Champion, pk=champion_id)
    return render(request, 'tft/detail.html', {'champion': champion})