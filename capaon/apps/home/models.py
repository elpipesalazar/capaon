from django.db import models

class Contenido(models.Model):
	titulo = models.CharField(max_length=100, primary_key=True)
	Descripcion= models.TextField()

	def __unicode__(self):
		return self.titulo