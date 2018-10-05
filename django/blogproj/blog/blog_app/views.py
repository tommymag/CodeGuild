from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from blog_app.forms import CreateBlogForm
from blog_app.models import Blog

def index(request):
	blogs = Blog.objects.all()

	return render(request, 'index.html', {'blogs': blogs})

def profile(request):
	is_blogger = request.user.groups.filter(name='Bloggers').exists()
	is_commenter = request.user.groups.filter(name='Commenters').exists()

	return render(request, 'profile.html', {'is_blogger': is_blogger, 'is_commenter': is_commenter})

def blog_create(request):
	form = CreateBlogForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			blog = form.save(commit=False)
			# commit=False tells Django that "Don't send this to database yet.
			# I have more things I want to do with it."
			blog.owner = request.user # Set the user object here
			blog.save() # Now you can send it to DB
			return HttpResponseRedirect('/')
	return render(request, 'create.html', {'form': form})

def blog(request, slug):
	blog = get_object_or_404(Blog, blog_slug=slug)
	return render(request, 'blog_content.html', {'blog':blog})






















