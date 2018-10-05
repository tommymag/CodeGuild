from django.urls import path
from blog_app import views

app_name = 'blog_app' # for namespacing

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('blog_create', views.blog_create, name='blog_create'),
    # path('blog/<int:pk>' views.blog, name='blog_content'),
    ]


