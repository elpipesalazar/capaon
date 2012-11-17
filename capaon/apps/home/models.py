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

class Objetivo(models.Model):
	Descripcion = models.TextField()


class Horario(models.Model):
	Dia = models.CharField(max_length=40, choices = dias)
	De = models.IntegerField()
	Hasta = models.IntegerField()


class Facilitador(models.Model):
	Nombre = models.CharField(max_length=100)
	Descripcion = models.TextField()


class Fase(models.Model):
	Descripcion = models.TextField()


class FasesModulo(models.Model):
	Nombre = models.CharField(max_length=100)
	Fases = models.ManyToManyField(Fase)


class Modulo(models.Model):
	Numero = models.IntegerField()
	Nombre = models.CharField(max_length=50)
	Duracion = models.IntegerField()
	Facilitador = models.ManyToManyField(Facilitador)
	Fases = models.ManyToManyField(FasesModulo)
	
class Curso(models.Model):
	Nombre = models.CharField(max_length=100, primary_key=True)
	Generalidades = models.TextField()
	Objetivos = models.ManyToManyField(Objetivo)
	Duracion = models.IntegerField()
	Horario = models.ForeignKey(Horario)
	Metodologia = models.TextField()
	Contenido = models.ForeignKey(Modulo)
	Estado = models.CharField(choices= EstadoCurso, max_length=50)
	CupoMin = models.IntegerField()
	CupoMax = models.IntegerField()
	Matriculados = models.ManyToManyField(Cliente)
	#Inscritos = models.ManyToManyField(Cliente)


class Empresa(models.Model):
	Nombre = models.CharField(max_length=100)
	NIT = models.CharField(max_length=100, primary_key=True)
	Telefono = models.CharField(max_length=30)
	Fax = models.CharField(max_length=30)
	Actividad = models.CharField(max_length=100)
	Pais = models.CharField(max_length=50, choices=pais)
	Direccion = models.CharField(max_length=150)
	Email = models.EmailField(unique=True)
	Estado = models.CharField(choices = estadoCliente, max_length=50)
	Potencial = models.BooleanField()
	
	def __unicode__(self):
		return self.Nombre


class Individual(models.Model):
	Nombre = models.CharField(max_length=100)
	Apellido = models.CharField(max_length=100)
	Email = models.EmailField()
	Cedula = models.CharField(max_length=100)
	FechaNacimiento = models.DateField()
	Direccion = models.CharField(max_length=100)
	Pais = models.CharField(choices=pais, max_length=50)
	Telefono = models.CharField(max_length=100)
	Celular = models.CharField(max_length=100)
   	Estado = models.CharField(choices = estadoCliente, max_length=50)
	Potencial = models.BooleanField()
	
	def __unicode__(self):
		return self.Nombre
