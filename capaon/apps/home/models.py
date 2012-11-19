from django.db import models

pais = (('Colombia','colombia'), ('Venezuela','venezuela'),('Brasil','brasil'))

dias = (('Lunes','Lunes'),('Martes','Martes'),('Miercoles','Miercoles'),('Jueves', 'Jueves'),
		('Viernes','Viernes'),('Sabado', 'Sabado'),	('Domingo', 'Domingo'))

EstadoCurso = (('En curso','En curso'), ('En Inscripciones','En Inscripciones'),('Cancelado','Cancelado'),
			   ('Terminado','Teminado'))

cliente = (('Individual','Individual'),('Empresarial','Empresarial'))

estadoCliente = (('Inscrito','Inscrito'),('Matriculado','Matriculado'))

class Contenido(models.Model):
	titulo = models.CharField(max_length=100, primary_key=True)
	Descripcion= models.TextField()

	def __unicode__(self):
		return self.titulo



class Contacto(models.Model):
	Empresa = models.CharField(max_length=100, primary_key=True)
	Pais = models.CharField(max_length=100)
	Ciudad = models.CharField(max_length=100)
	Telefono = models.CharField(max_length=50)
	Email = models.EmailField()

	def __unicode__(self):
		return self.Empresa


class Horario(models.Model):
	Dia = models.CharField(max_length=40, choices = dias)
	De = models.CharField(max_length=40)
	Hasta = models.CharField(max_length=40)

	def __unicode__(self):
		return self.Dia + " " + self.De + " a " + self.Hasta


class Facilitador(models.Model):
	Nombre = models.CharField(max_length=100, unique=True)
	Descripcion = models.TextField(blank=True)

	def __unicode__(self):
		return self.Nombre
	class Admin:
		list_display = ('Nombre')
		list_filter = ('Nombre')
		ordering = ('-Nombre')
		search_fields = ('Nombre')

	
class Cliente(models.Model):
	Estado = models.CharField(choices = estadoCliente, max_length=50)
	Potencial = models.BooleanField()

class Inscrito(models.Model):
	cliente = models.ForeignKey(Cliente)
	fechaInscripcion = models.DateTimeField(auto_now_add=True)

class Matriculado(models.Model):
	cliente = models.ForeignKey(Cliente)
	fechaMatricula = models.DateTimeField(auto_now_add=True)

class Curso(models.Model):
	Nombre = models.CharField(max_length=100, unique=True)
	Generalidades = models.TextField()
	Objetivos = models.TextField()
	Duracion = models.IntegerField(help_text="Horas")
	Horario = models.ManyToManyField(Horario)
	Metodologia = models.TextField()
	Estado = models.CharField(choices= EstadoCurso, max_length=50)
	CupoMin = models.IntegerField()
	CupoMax = models.IntegerField()
	Inscritos = models.ManyToManyField(Inscrito, editable=False, blank=True)
	Matriculados = models.ManyToManyField(Matriculado, editable=False, blank=True)

	class Admin:
		list_display = ('Nombre', 'Duracion', 'Estado')
		list_filter = ('Duracion', 'Estado')
		ordering = ('-Estado',)
		search_fields = ('Nombre',)

	def __unicode__(self):
		return self.Nombre

class Modulo(models.Model):
	Numero = models.IntegerField()
	Nombre = models.CharField(max_length=150, unique=True)
	Duracion = models.IntegerField()
	Facilitador = models.ForeignKey(Facilitador, blank=True)
	Contenido = models.TextField()
	Curso = models.ForeignKey(Curso)

	class Admin:
		list_display = ('Numero', 'Nombre', 'Facilitador')
		list_filter = ('Nombre', 'Facilitador')
		ordering = ('-Curso',)
		search_fields = ('Nombre',)

	def __unicode__(self):
		return self.Nombre


class Empresa(models.Model):	
	RazonSocial = models.CharField(max_length=100)
	NIT = models.CharField(max_length=100, primary_key=True)
	Direccion = models.CharField(max_length=150)
	Actividad = models.CharField(max_length=100)
	Telefono = models.CharField(max_length=30)
	Fax = models.CharField(max_length=30)
	Email = models.EmailField(unique=True)
	Pais = models.CharField(max_length=50, choices=pais)
	
	def __unicode__(self):
		return self.Nombre


class Individual(models.Model):
	Nombre = models.CharField(max_length=100)
	Apellido = models.CharField(max_length=100)
	Cedula = models.CharField(max_length=100)
	Direccion = models.CharField(max_length=100)
	FechaNacimiento = models.DateField()
	Telefono = models.CharField(max_length=30)
	Celular = models.CharField(max_length=100)
	Email = models.EmailField(unique=True)
	Pais = models.CharField(max_length=50, choices=pais)
	
	def __unicode__(self):
		return self.Nombre + self.Apellido