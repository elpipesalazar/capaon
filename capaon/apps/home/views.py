from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from capaon.apps.home.models import Contenido, Contacto, Curso, Modulo
from capaon.apps.home.forms import EmpresaForm, ContactForm


#vista del index (pagina incial)
def index_view(request):
	titulo = "Capacitaciones Online - CAPAON"
	quienesSomos = Contenido.objects.filter(titulo = 'Quienes Somos')
	contacto = Contacto.objects.all()
	cursos = Curso.objects.all()
	return render_to_response('index.html',locals(),context_instance = RequestContext(request))

#vista de Registro de Usuario
def register_view(request):
	Empresaform = EmpresaForm()
	contacto = Contacto.objects.all()
	if request.method == 'POST':
		datos = request.POST.copy()
		errores = Empresaform.get_validation_errors(datos)
	ctx = {"EmpresaForm": Empresaform}
	return render_to_response('register.html', ctx, context_instance = RequestContext(request))

#vista de mision y vision
def mv_view(request):
	Mision = Contenido.objects.filter(titulo = 'Mision')
	Vision = Contenido.objects.filter(titulo = 'Vision')
	contacto = Contacto.objects.all()
	return render_to_response('MisionVision.html', locals() , context_instance = RequestContext(request))

#Vista de la seccion Contactenos
def contact_view(request):
	contacto = Contacto.objects.filter(Empresa = 'CI')
	if request.method =='POST':
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			titulo = "Mensaje Enviado desde CAPAON"
			contenido = formulario.cleaned_data['Mensaje'] + "\n"
			remitente = formulario.cleaned_data['Email']
			contenido += 'Comunicarse a: ' + remitente + "\n"
			contenido += 'Nombre de Remitente: ' + formulario.cleaned_data['Nombre'] + "\n"
			contenido += 'Ciudad: ' + formulario.cleaned_data['Ciudad']
			send_mail(titulo, contenido, remitente, ['elpipesalazar@hotmail.com'], fail_silently=False)	
			return HttpResponseRedirect('/')
	else:
		formulario = ContactForm()
	return render_to_response('contact.html',locals(),context_instance = RequestContext(request))

#Vista de la Seccion de Capacitacion
def cursos_view(request):
	cursos = Curso.objects.all()
	contacto = Contacto.objects.all()
	return render_to_response('cursos.html',locals(),context_instance = RequestContext(request))

def Infocursos_view(request, idn):
	try:
		contacto = Contacto.objects.all()
 		curso = Curso.objects.get(id = idn)
 		horario = curso.Horario.all()
 		modulos = Modulo.objects.filter(Curso__id__exact = idn)
 	except Curso.DoesNotExist:
 		curso = False
 	return render_to_response('infocurso.html',locals(), context_instance = RequestContext(request))

def construccion(request):
	return render_to_response('404.html', context_instance = RequestContext(request))