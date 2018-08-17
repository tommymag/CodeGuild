from django.urls import path
from . import views

urls_app = 'urls_app' # for namespacing
urlpatterns = [
    path('', views.index, name='index')
]