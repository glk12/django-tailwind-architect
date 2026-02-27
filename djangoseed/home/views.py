from django.shortcuts import render
from .models import About, Hero, Logo

def	home(request):
	about = About.objects.first()
	hero = Hero.objects.first()
	logo = Logo.objects.first()
	return render(request, 'home/home.html',{'about': about, 'hero': hero, 'logo' : logo})
