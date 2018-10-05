from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Blog(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	bio_text = models.TextField(max_length=511,)
	blog_slug = models.SlugField()
	blog_title = models.CharField(max_length=255, )
	summary = models.TextField()

	def __str__(self):
		"""String for representing the Model object."""
		return self.blog_title

class Post(models.Model):
	# author = models.ForeignKey(User, on_delete=models.CASCADE)
	post_title = models.CharField(max_length=255, )
	text = models.TextField()
	date_created = models.DateField(default=datetime.now)#sort
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

	def __str__(self):
		"""String for representing the Model object."""
		return self.post_title

# class Comment(models.Model):
# 	post.id =
# 	user.id =
# 	date.created = 		#sort


# class Author(models.Model):
#     """Model representing an author."""
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     date_of_birth = models.DateField(null=True, blank=True)
#     date_of_death = models.DateField('Died', null=True, blank=True)

#     class Meta:
#         ordering = ['last_name', 'first_name']

    
#     def get_absolute_url(self):
#         """Returns the url to access a particular author instance."""
#         return reverse('author-detail', args=[str(self.id)])

#     def __str__(self):
#         """String for representing the Model object."""
#         return f'{self.last_name}, {self.first_name}'