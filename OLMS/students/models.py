from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	summary = models.TextField()
	ISBN = models.CharField(max_length=13)
	publish_year = models.IntegerField()
	pic = models.ImageField(upload_to='book_image', blank=True)
	return_date = models.DateField(blank=True, null=True)
	status = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return f"{self.title}"