from django.db import models

class Logo(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='nav/logo')

	def __str__(self):
		return self.title

class About(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	image = models.ImageField(upload_to='about/', blank=True, null=True)

	def __str__(self):
		return self.title

class Hero(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	image = models.ImageField(upload_to='hero/')

	def __str__(self):
		return self.title
