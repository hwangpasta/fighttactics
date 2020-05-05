from django.http import HttpResponse, request


def index(request):
    return HttpResponse("Teamfight Tactics")

def champion(request, champion_id):
    response = "You're looking at the champion page."
    return HttpResponse(response % champion_id)