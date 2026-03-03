from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About, Hero, Logo
from .forms import ContactDjangoForms
def	home(request):
	about = About.objects.first()
	hero = Hero.objects.first()
	logo = Logo.objects.first()

	if request.method == 'POST':
		form = ContactDjangoForms(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Seu orçamento foi enviado com sucesso!')
			return redirect('/#contato')
	else:
		form = ContactDjangoForms()
	return render(request, 'home/home.html',{'about': about, 'hero': hero, 'logo' : logo, 'form': form})
