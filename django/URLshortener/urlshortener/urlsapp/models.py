from django.db import models

# Create your models here.
class URL(models.Model):
	url_long = models.CharField(max_length=250, unique=True)
	url_short = models.CharField(max_length=10, primary_key=True)

	def __str__(self):
		return url