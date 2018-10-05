from django import forms
from blog_app.models import Blog

class CreateBlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ['bio_text', 'blog_slug', 'blog_title', 'summary']

