from django.db import models

pais = (('Colombia','colombia'), 
		('Venezuela','venezuela'), 
		('Brasil','brasil'))

dias = (('Lunes','Lunes'),
		('Martes','Martes'),
		('Miercoles','Miercoles'),
		('Jueves', 'Jueves'),
		('Viernes','Viernes'),
		('Sabado', 'Sabado'),
		('Domingo', 'Domingo'))

EstadoCurso = (('En curso','En curso'),
			   ('En Inscripciones','En Inscripciones'),
			   ('Cancelado','Cancelado'),
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
	Dia = models.CharField(choices = dias)
	De = models.IntegerField()
	Hasta = models.IntegerField()


class Facilitador(models.Model):
	Nombre = models.CharField(max_length=100)
	Descripcion = models.TextField()


class Fases(models.Model):
	Descripcion = models.TextField()


class FasesModulo(models.Model):
	Nombre = models.CharField(max_length=100)
	Fases = models.ManyToManyField(Fases)


class Modulos(models.Model):
	Numero = models.IntegerField()
	Nombre = models.CharField()
	Duracion = models.IntegerField()
	Facilitador = models.ManyToManyField(Facilitador)
	Fases = models.ManyToManyField(FasesModulo)


class EstadosCurso(models.Model):
	tipo = models.CharField(choices= EstadoCurso)


class Cliente(models.Model):
	Tipo = models.CharField(choices=cliente)
	#Curso = models.ManyToManyField(Curso)
	Estado = models.CharField(choices = estadoCliente)
	Potencial = models.BooleanField()
	
class Curso(models.Model):
	Nombre = models.CharField(max_length=100, primary_key=True)
	Generalidades = models.TextField()
	Objetivos = models.ManyToManyField(Objetivo)
	Duracion = models.IntegerField()
	Horario = models.ForeignKey(Horario)
	Metodologia = models.TextField()
	Contenido = models.ForeignKey(Modulos)
	Estado = models.ForeignKey(EstadosCurso)
	CupoMin = models.IntegerField()
	CupoMax = models.IntegerField()
	Matriculados = models.ManyToManyField(Cliente)
	Inscritos = models.ManyToManyField(Cliente)


class Empresa(models.Model):
	Nombre = models.CharField(max_length=100)
	NIT = models.CharField(max_length=100, primary_key=True)
	Telefono = models.CharField(max_length=30)
	Fax = models.CharField(max_length=30)
	Actividad = models.CharField(max_length=100)
	Pais = models.CharField(max_length=50, choices=pais)
	Direccion = models.CharField(max_length=150)
	Email = models.EmailField(unique=True)

	def __unicode__(self):
		return self.Nombre


class Indivudual(models.Model):
	Nombre = models.CharField(max_length=100)
	Apellido = models.CharField(max_length=100)
	Email = models.EmailField()
	Cedula = models.CharField(max_length=100)
	FechaNacimiento = models.DateField()
	Direccion = models.CharField(max_length=100)
	Pais = models.CharField(choices=pais)
	Telefono = models.CharField(max_length=100)
	Celular = models.CharField(max_length=100)

	def __unicode__(self):
		return self.Nombre
