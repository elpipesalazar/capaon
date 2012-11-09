from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from capaon.apps.home.models import Contenido

#vista del index (pagina incial)
def index_view(request):
	titulo = "Capacitaciones Online - CAPAON"
	Mision = Contenido.objects.filter(titulo = 'Mision')
	ctx = {'titulo':titulo, 'Mision':Mision}
	return render_to_response('index.html',ctx,context_instance = RequestContext(request))

#vista de Registro de Usuario
def register_view(request):
	return render_to_response('register.html', context_instance = RequestContext(request))

#vista de Quienes Somos
def about_view(request):
	QuienesSomos = Contenido.objects.filter(titulo = 'Quienes Somos')
	ctx = {'QuienesSomos':QuienesSomos}
	return render_to_response('about.html', ctx , context_instance = RequestContext(request))

#vista de mision y vision
def mv_view(request):
	Mision = Contenido.objects.filter(titulo = 'Mision')
	Vision = Contenido.objects.filter(titulo = 'Vision')
	ctx = {'Mision': Mision , 'Vision': Vision}
	return render_to_response('MisionVision.html', ctx , context_instance = RequestContext(request))

def contact_view(request):
	return render_to_response('contact.html',context_instance = RequestContext(request))