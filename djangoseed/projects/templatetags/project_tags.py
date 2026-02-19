from django import template
from django.db.models import Prefetch

from projects.models import Project, ProjectImage

register = template.Library()


@register.inclusion_tag('projects/projects.html')
def render_projects_list():
	projects = (
		Project.objects
		.prefetch_related(Prefetch('images', queryset=ProjectImage.objects.all()))
	)
	return {'projects': projects}
