from django.contrib import admin
from .models import Project, ProjectImage


class ProjectImageInline(admin.TabularInline):
	model = ProjectImage
	extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at')
	list_filter = ('created_at',)
	search_fields = ('title',)
	inlines = [ProjectImageInline]


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
	list_display = ('project', 'caption', 'order')
	list_filter = ('project',)
