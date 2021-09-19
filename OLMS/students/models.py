from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=70)
	summary = models.TextField()
	ISBN = models.CharField(max_length=13)
	publish_year = models.IntegerField()
	pic = models.ImageField(upload_to='book_image', blank=True)


	def __str__(self):
		return f"{self.title}"