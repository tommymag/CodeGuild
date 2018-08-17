from django.urls import path
from . import views

app_name = 'todos'
# These urls are relative to the line 20 on the left
urlpatterns = [
	path('', views.index_view, name='index_path'),
	path('add_url/', views.add_view, name='add'),
	path('delete/<int:pk>/', views.delete, name='delete'),
	path('markdone/<int:pk>/', views.markdone, name='markdone'),
	path('django_form_index/', views.index_with_django_form, name='form_index'),
	path('model_form_index/', views.index_with_model_form, name='model_index'),
]