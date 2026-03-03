from django.contrib import admin
from .models import About, Hero, Logo, ContactForm

admin.site.register(About)
admin.site.register(Hero)
admin.site.register(Logo)

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
	list_display = ("   name", "email", "telephone", "sent_at")
	search_fields = ("name", "email", "telephone")
	ordering = ("-sent_at",)