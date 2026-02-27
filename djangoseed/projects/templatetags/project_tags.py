from django import template
from django.db.models import Prefetch

from projects.models import Project, ProjectImage

register = template.Library()

# Resolução padronizada para fotos na galeria (aspect 4:3, retina-friendly)
PROJECT_IMAGE_WIDTH = 1200
PROJECT_IMAGE_HEIGHT = 900


@register.filter
def cloudinary_thumb(url, size=None):
	"""Insere transformação Cloudinary para thumbnail padronizado. Usa c_fit (fit inside) para não cortar."""
	if not url or 'cloudinary.com' not in str(url):
		return url
	w, h = (size.split('x') if size else [PROJECT_IMAGE_WIDTH, PROJECT_IMAGE_HEIGHT])[:2]
	# q_85 = qualidade alta, f_auto = WebP quando suportado (sem perda perceptível)
	transform = f"c_fit,w_{w},h_{h},q_85,f_auto"
	# Insere transformação logo após /image/upload/
	if '/image/upload/' in url:
		return url.replace('/image/upload/', f'/image/upload/{transform}/')
	return url


@register.inclusion_tag('projects/projects.html')
def render_projects_list():
	projects = (
		Project.objects
		.prefetch_related(Prefetch('images', queryset=ProjectImage.objects.all()))
	)
	return {'projects': projects}
