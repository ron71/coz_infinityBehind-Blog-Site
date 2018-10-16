from django.db import models

# Create your models here.

class Post(models.Model):

	title = models.CharField(max_length=140)
	post_tag = models.CharField(max_length=20, null=True, blank=True)
	body = models.TextField()
	date = models.DateTimeField()
	
	def __str__(self):
		return self.title



