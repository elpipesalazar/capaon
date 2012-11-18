from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from capaon.apps.home.models import Contenido, Contacto, Curso
from capaon.apps.home.forms import EmpresaForm

#vista del index (pagina incial)
def index_view(request):
	num = 1
	titulo = "Capacitaciones Online - CAPAON"
	quienesSomos = Contenido.objects.filter(titulo = 'Quienes Somos')
	cursos = Curso.objects.all()
	return render_to_response('index.html',locals(),context_instance = RequestContext(request))

#vista de Registro de Usuario
def register_view(request):
	Empresaform = EmpresaForm()
	if request.method == 'POST':
		datos = request.POST.copy()
		errores = Empresaform.get_validation_errors(datos)
	ctx = {"EmpresaForm": Empresaform}
	return render_to_response('register.html', ctx, context_instance = RequestContext(request))

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
	contacto = Contacto.objects.filter(Empresa = 'CI')
	ctx = {'datos':contacto}
	return render_to_response('contact.html',ctx,context_instance = RequestContext(request))

def construccion(request):
	return render_to_response('404.html', context_instance = RequestContext(request))