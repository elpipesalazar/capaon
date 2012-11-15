from django.db import models

pais = (('Colombia','colombia'), 
		('Venezuela','venezuela'), 
		('Brasil','brasil'))

class Contenido(models.Model):
	titulo = models.CharField(max_length=100, primary_key=True)
	Descripcion= models.TextField()

	def __unicode__(self):
		return self.titulo

class Empresa(models.Model):
	Nombre = models.CharField(max_length=100)
	NIT = models.CharField(max_length=100, primary_key=True)
	Telefono = models.CharField(max_length=30)
	Fax = models.CharField(max_length=30)
	Actividad = models.CharField(max_length=100)
	Pais = models.CharField(max_length=50, choices=pais)
	Direccion = models.CharField(max_length=150)
	Email = models.EmailField(unique=True)


class Contacto(models.Model):
	Empresa = models.CharField(max_length=100, primary_key=True)
	Pais = models.CharField(max_length=100)
	Ciudad = models.CharField(max_length=100)
	Telefono = models.CharField(max_length=50)
	Email = models.EmailField()

	def __unicode__(self):
		return self.Empresa

class Curso(models.Model):
	Nombre = models.CharField(max_length=100)
