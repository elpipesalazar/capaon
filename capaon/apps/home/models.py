from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import watson
import datetime

# Tuplas que son Utilizadas en los modelos de datos

pais = (('Colombia','colombia'), ('Venezuela','venezuela'),('Brasil','brasil'))
dias = (('Lunes','Lunes'),('Martes','Martes'),('Miercoles','Miercoles'),('Jueves', 'Jueves'),('Viernes','Viernes'),('Sabado', 'Sabado'),	('Domingo', 'Domingo'))
EstadoCurso = (('En curso','En curso'), ('En Inscripciones','En Inscripciones'),('Cancelado','Cancelado'),('Terminado','Teminado'))
cliente = (('Individual','Individual'),('Empresarial','Empresarial'))
estadoCliente = (('Inscrito','Inscrito'),('Matriculado','Matriculado'))


# En este modelo se agrega el contenido principal de la plataforma
# Entre ellos esta, Mision, Vision y Quienes Somos
class DatosEmpresa(models.Model):
	titulo 		= 	models.CharField(max_length=100, primary_key=True, help_text='Por favor,No edite este titulo')
	Contenido 	= 	models.TextField(help_text='Agregue el Contenido')

	class Meta:
		verbose_name_plural="Datos del home"
	def __unicode__(self):
		return self.titulo


# Este modelo contiene los datos de contacto de la Empresa
# Estos datos son mostrados en la seccion Contactame y en el pie de pagina de cada seccion
class Contacto(models.Model):
	empresa 	= 	models.CharField(max_length=100, primary_key=True, help_text='Nombre de la Empresa')
	pais 		= 	models.CharField(max_length=100, choices=pais)
	ciudad 		= 	models.CharField(max_length=100)
	telefono 	= 	models.CharField(max_length=50)
	email 		= 	models.EmailField(help_text='correo@example.com')

	class Meta:
		verbose_name_plural=u'Datos De Contacto Capaon'
	def __unicode__(self):
		return self.empresa


# Modelo para definir los horarios de los cursos
class Horario(models.Model):
	dia 	= 	models.CharField(max_length=40, choices = dias)
	de 		=	models.CharField(max_length=40,help_text='Escribe la hora ej: 2:00 p.m.')
	hasta 	= 	models.CharField(max_length=40,help_text='Escribe la hora ej: 2:00 p.m.')

	def __unicode__(self):
		return self.dia + " " + self.de + " a " + self.hasta



# Modelo para especificar el nombre y la descripcion del Facilitador de un curso
class Facilitador(models.Model):
	nombre 			= 	models.CharField(max_length=100, unique=True)
	descripcion 	= 	models.TextField(blank=True, help_text='Describa al Facilitador')

	class Meta:
		verbose_name_plural = "Facilitadores"
	def __unicode__(self):
		return self.nombre
	


class Curso(models.Model):
	nombre 				= 	models.CharField(max_length=100, unique=True, help_text='Nombre de Curso', null=False)
	generalidades 		= 	models.TextField()
	objetivos 			= 	models.TextField(help_text='Escriba cada objetivo separado por un salto de linea, si es subindice, agregue un guion')
	duracion 			= 	models.IntegerField(help_text="Horas. Ej: 12")
	horario 			= 	models.ManyToManyField(Horario, help_text='Asigne uno o varios horarios')
	metodologia 		=	models.TextField()
	estado 				= 	models.CharField(choices= EstadoCurso, max_length=50, blank=True)
	cupoMin 			= 	models.IntegerField(default=20)
	cupoMax 			= 	models.IntegerField(default=30)
	#cuposDisponible		=	models.IntegerField()
	inicioInscripciones = 	models.DateField(auto_now=True, help_text='Feha Inicial Para Inscripciones')
	finalInscripciones 	= 	models.DateField(help_text='Fecha Final para Inscripciones (La fecha de Inicio empieza al crear este curso)')
	fechaInicio 		= 	models.DateField(help_text='Fecha de Inicio de curso')
	fechaFinal 			= 	models.DateField(help_text='Fecha de Finalizacion de curso')

	def __unicode__(self):
		return self.nombre

# modelo para guardar los clientes que se han inscrito en alguno de los cursos ofertados
class Inscrito(models.Model):
	curso 				= 	models.ForeignKey(Curso, null=True)
	cliente 			= 	models.ForeignKey(User, help_text='Escoja un cliente de la lista', null=True)
	fechaInscripcion 	= 	models.DateField(auto_now_add=True,null=True)
	FechaCaducidad 		= 	models.DateField(null=True)

	def __unicode__(self):
		return self.cliente.get_profile().nombre + " " + self.cliente.get_profile().apellidos  


# modelo para guardar los clientes que se han matriculado en alguno de los cursos ofertados
class Matriculado(models.Model):
	curso 				= 	models.ForeignKey(Curso, null=True)
	cliente 			= 	models.ForeignKey(User, help_text='Escoja un cliente de la lista', null=True)
	fechaMatricula 		= 	models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.cliente.get_profile().nombre + " " + self.cliente.get_profile().apellidos  


class Modulo(models.Model):
	numero 		= 	models.IntegerField(help_text='Numero del modulo del curso')
	nombre 		= 	models.CharField(max_length=150, unique=True, help_text='Nombre del modulo')
	duracion 	=	models.IntegerField(help_text='Ingrese un entero con el valor de las horas de duracion ej: 25')
	facilitador = 	models.ForeignKey(Facilitador,null=True, help_text='Escoja un facilitador')
	contenido 	= 	models.TextField(help_text='Ingrese el contenido separando cada apartado con un salto de linea')
	curso 		= 	models.ForeignKey(Curso, help_text='Escoje el curso al cual pertenece este modulo')

	def __unicode__(self):
		return self.nombre


# Los modelos de Usuario Individual y Empresarial son iniciales y no se han optimizado
# Esta tarea se hara en el segundo release


class PerfilCliente(models.Model):
	user 			= 	models.ForeignKey(User, related_name='perfil', unique=True)
	nombre 			= 	models.CharField(max_length=50)
	apellidos 		= 	models.CharField(max_length=60)
	email 			= 	models.EmailField()
	cedula 			= 	models.CharField(max_length=100)
	direccion 		= 	models.CharField(max_length=100, blank=True)
	fechaNacimiento = 	models.DateField(null=True, blank=True)
	telefono 		=	models.CharField(max_length=30, blank=True)
	celular  		= 	models.CharField(max_length=100)
	ciudad 			= 	models.CharField(max_length=50, blank=True)
	pais 			= 	models.CharField(max_length=50, choices=pais)

	class Meta:
         verbose_name = "PerfilCliente"
	
	def __unicode__(self):
		return self.nombre + " " + self.apellidos

class Empresa(models.Model):	
	razonSocial 	= 	models.CharField(max_length=100)
	nit 			= 	models.CharField(max_length=100, primary_key=True)
	actividad 		= 	models.CharField(max_length=100)
	fax 			= 	models.CharField(max_length=30)
	representante 	= 	models.ForeignKey(PerfilCliente, unique=True)
	
	def __unicode__(self):
		return self.razonSocialcd

class Cliente(models.Model):
	perfil 		= 	models.ForeignKey(PerfilCliente, unique=True)
	tipo 		= 	models.CharField(max_length=50)
	potencial 	= 	models.BooleanField(default=False)

	class Meta:
		verbose_name_plural = "Definir Potenciales"

watson.register(DatosEmpresa)
watson.register(Horario)
watson.register(Curso)
watson.register(Modulo)