from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
	todo_text = models.CharField(max_length=250, unique=True)
	completed = models.BooleanField(default=False)
	created_date = models.DateTimeField(default=datetime.now())
	user = models.ForeignKey(User, on_delete='CASCADE')

	def __str__(self):
		return self.todo_text