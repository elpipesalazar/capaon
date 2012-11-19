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
