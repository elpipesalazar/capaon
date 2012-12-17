from django.shortcuts import render_to_response
from django.template import RequestContext 
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm 
from capaon.apps.home.models import DatosEmpresa, Contacto, Curso, Modulo, Empresa, PerfilCliente, Cliente, Inscrito, Matriculado
from capaon.apps.home.forms import ClienteForm, ContactForm, EmpresaForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
import watson
import datetime
from django.utils.timezone import is_aware, utc



#vista del index (pagina incial)
def index_view(request):
	loginInvalido = False;
	titulo = "Capacitaciones Online - CAPAON"
	quienesSomos = DatosEmpresa.objects.filter(titulo = 'Quienes Somos')
	contacto = Contacto.objects.all()
	cursos = Curso.objects.all()
	return render_to_response('index.html',locals(),context_instance = RequestContext(request))

#vista de Registro de Usuario
def register_view(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	contacto = Contacto.objects.all()
	return render_to_response('register.html', locals(), context_instance = RequestContext(request))

def registrar_empresa(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	contacto = Contacto.objects.all()
	if request.method == 'POST':
		cliente = ClienteForm(request.POST)
		empresaform = EmpresaForm(request.POST)
		if cliente.is_valid() and empresaform.is_valid():
			user = User.objects.create_user(username=cliente.cleaned_data['username'], email = cliente.cleaned_data['email'], password = cliente.cleaned_data['password'])
			user.first_name = cliente.cleaned_data['nombre'] 
			user.last_name = cliente.cleaned_data['apellidos']
			user.save()
			clienteEmpresa = PerfilCliente(user = user, nombre = cliente.cleaned_data['nombre'], apellidos = cliente.cleaned_data['apellidos'] , email = cliente.cleaned_data['email'],cedula = cliente.cleaned_data['cedula'], direccion = cliente.cleaned_data['direccion'], fechaNacimiento = cliente.cleaned_data['fechaNacimiento'], telefono = cliente.cleaned_data['telefono'], celular = cliente.cleaned_data['celular'], ciudad = cliente.cleaned_data['ciudad'],pais = cliente.cleaned_data['pais'])
			clienteEmpresa.save()
			empresa = Empresa(razonSocial = empresaform.cleaned_data['razonSocial'], nit = empresaform.cleaned_data['nit'], actividad = empresaform.cleaned_data['actividad'], fax = empresaform.cleaned_data['fax'], representante = clienteEmpresa)
			empresa.save()
			cliente = Cliente(perfil = clienteEmpresa, tipo = "Empresa")
			cliente.save()
			return  HttpResponseRedirect('/')
	else:		
		empresa = EmpresaForm()
		cliente = ClienteForm()
	return render_to_response('registroEmpresa.html', locals(), context_instance = RequestContext(request))

def registrar_individual(request):
	contacto = Contacto.objects.all()
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	if request.method == 'POST':
		cliente = ClienteForm(request.POST)
		if cliente.is_valid():
			user = User.objects.create_user(username=cliente.cleaned_data['username'], email = cliente.cleaned_data['email'], password = cliente.cleaned_data['password'])
			user.first_name = cliente.cleaned_data['nombre'] 
			user.last_name = cliente.cleaned_data['apellidos']
			user.save()
			clienteIndividual = PerfilCliente(user = user, nombre = cliente.cleaned_data['nombre'], apellidos = cliente.cleaned_data['apellidos'] , email = cliente.cleaned_data['email'],cedula = cliente.cleaned_data['cedula'], direccion = cliente.cleaned_data['direccion'], fechaNacimiento = cliente.cleaned_data['fechaNacimiento'], telefono = cliente.cleaned_data['telefono'], celular = cliente.cleaned_data['celular'], pais = cliente.cleaned_data['pais'])
			clienteIndividual.save()
			cliente = Cliente(perfil = clienteIndividual, tipo = "Individual")
			cliente.save()
			return  HttpResponseRedirect('/')
	else:
		cliente = ClienteForm()
	return render_to_response('registroIndividual.html', locals(), context_instance = RequestContext(request))



#vista de mision y vision
def mv_view(request):
	Mision = DatosEmpresa.objects.filter(titulo = 'Mision')
	Vision = DatosEmpresa.objects.filter(titulo = 'Vision')
	contacto = Contacto.objects.all()
	return render_to_response('MisionVision.html', locals() , context_instance = RequestContext(request))

#Vista de la seccion Contactenos
def contact_view(request):
	contacto = Contacto.objects.all()
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
 		horario = curso.horario.all()
 		modulos = Modulo.objects.filter(curso__id__exact = idn)
 		if request.user.is_authenticated() and not request.user.is_staff:
 			estaInscrito = Inscrito.objects.filter(cliente = request.user)
 	except Curso.DoesNotExist:
 		curso = False
 	return render_to_response('infocurso.html',locals(), context_instance = RequestContext(request))



def inscripcion_view(request, idc):
	if request.user.is_authenticated() and not request.user.is_staff:
		fechaInscripcion = datetime.datetime.now(utc)
		fechaCaducidad = datetime.datetime(fechaInscripcion.year , fechaInscripcion.month, fechaInscripcion.day + 1)
		curso = Curso.objects.get(id__exact = idc)
		if curso:
			nuevoInscrito = Inscrito(curso = curso,cliente =request.user, fechaInscripcion = fechaInscripcion, FechaCaducidad = fechaCaducidad)
			nuevoInscrito.save()
			return HttpResponseRedirect('/miscursos/')
	return HttpResponseRedirect('/')


def miscursos_view(request):
	if request.user.is_authenticated() and not request.user.is_staff:
		misInscritos    = Inscrito.objects.filter(cliente = request.user)
		misMatriculados = Matriculado.objects.filter(cliente = request.user) 
		return render_to_response("miscursos.html", locals(), context_instance = RequestContext(request))
	return HttpResponseRedirect('/')
		



def construccion(request):
	return render_to_response('404.html', context_instance = RequestContext(request))

def search_view(request):
	search_results = watson.search('somos')
	return render_to_response('search.html', locals(), context_instance = RequestContext(request))

def login_view(request):
	try:
		nickname = request.POST['nickname']
		password = request.POST['password']
		usuario = authenticate(username=nickname, password=password)
		if usuario is not None and usuario.is_active:
			login(request,usuario)
			return HttpResponseRedirect('/')
	except:
		return HttpResponseRedirect('/')
	titulo = "Capacitaciones Online - CAPAON"
	loginInvalido = True;
	quienesSomos = DatosEmpresa.objects.filter(titulo = 'Quienes Somos')
	contacto = Contacto.objects.all()
	cursos = Curso.objects.all()
	return render_to_response('index.html',locals(),context_instance = RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def profile_view(request):
	return render_to_response('perfil.html', context_instance = RequestContext(request))