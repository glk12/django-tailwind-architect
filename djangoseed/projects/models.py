from django.db import models


class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	cover_image = models.ImageField(upload_to='projects/cover', verbose_name="Imagem de capa")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Projeto"
		verbose_name_plural = "Projetos"
		ordering = ['created_at']

	def __str__(self):
		return self.title


class ProjectImage(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
	image = models.ImageField(upload_to='projects/gallery', verbose_name="Imagem")
	caption = models.CharField(max_length=200, blank=True)
	order = models.PositiveIntegerField(default=0)

	class Meta:
		verbose_name = "Imagem do Projeto"
		verbose_name_plural = "Imagens do Projeto"
		ordering = ['order']

	def __str__(self):
		return f"{self.project.title} - #{self.order}"
