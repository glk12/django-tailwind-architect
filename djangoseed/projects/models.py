from django.db import models


class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	cover_image = models.ImageField( upload_to='projects/cover', verbose_name="Imagem de capa")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Projeto"
		verbose_name_plural = "Projetos"
		ordering = ['-created_at']

	def __str__(self):
		return self.title
