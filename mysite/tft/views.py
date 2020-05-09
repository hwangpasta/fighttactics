from django.http import HttpResponse, request
from django.template import loader
from .models import Champion

def index(request):
    champion_list = Champion.
    template = loader.get_template('tft/index.html')
    context = {'champion_list': champion_list}
    return HttpResponse(template.render(context,request))

def Champion(request, champion_id):
    response = "You're looking at the champion page."
    return HttpResponse(response % champion_id)