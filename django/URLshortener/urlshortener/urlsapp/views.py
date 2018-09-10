from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import URL
import random, string

# Create your views here.

def index(request):
    url_list = URL.objects.all()
    context = {"web_address": url_list}
    if request.method == "POST":
        short_url = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
        long_url = request.POST['full_url']
        if URL.objects.filter(url_long=long_url).exists():
            return render(request, 'urlsapp/index.html', context)
        new_url = URL(url_long=long_url, url_short=short_url)
        new_url.save()
    return render(request, 'urlsapp/index.html', context)

def redirect(request, url_short):
    target_url = get_object_or_404(URL, url_short=url_short)
    return HttpResponseRedirect(target_url.url_long)

def redirect_typed(request):
    url_short = request.GET['short_url']
    target_url = get_object_or_404(URL, url_short=url_short)
    return HttpResponseRedirect(target_url.url_long)