from django.db import models

class Logo(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='nav/logo')

	def __str__(self):
		return self.title

class About(models.Model):
	class Meta:
		verbose_name = "Sobre nós"
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

class ContactForm(models.Model):
	class Meta:
		verbose_name = "Forms de Contato"
	name = models.CharField(max_length=200)
	email = models.EmailField()
	telephone = models.CharField(max_length=12, blank=True, null=True)
	message = models.TextField(blank = False)
	sent_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Mensagem do {self.name}"