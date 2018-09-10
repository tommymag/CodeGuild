from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from OOPDFapp.models import Flashcard
from django.core import serializers

# Create your views here.
def index(request):

    context = {
        'flashcards' : Flashcard.objects.all().order_by('?')
    }
    return render(request, 'OOPDFapp/index.html', context=context)

def flashcard_json(request):
    data = serializers.serialize("json", Flashcard.objects.all().order_by('?'))
    return JsonResponse(data, safe=False)

# def game_start(request):
#     pass


