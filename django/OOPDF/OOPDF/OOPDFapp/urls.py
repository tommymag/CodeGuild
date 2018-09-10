from django.urls import path
from . import views

app_name = 'OOPDFapp' # for namespacing	

urlpatterns = [
    path('', views.index, name='index'),
    path('flashcards/', views.flashcard_json, name='flashcard_api')
    
]