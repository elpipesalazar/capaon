from django.db import models

# Tuplas que son Utilizadas en los modelos de datos

pais = (('Colombia','colombia'), ('Venezuela','venezuela'),('Brasil','brasil'))
dias = (('Lunes','Lunes'),('Martes','Martes'),('Miercoles','Miercoles'),('Jueves', 'Jueves'),('Viernes','Viernes'),('Sabado', 'Sabado'),	('Domingo', 'Domingo'))
EstadoCurso = (('En curso','En curso'), ('En Inscripciones','En Inscripciones'),('Cancelado','Cancelado'),('Terminado','Teminado'))
cliente = (('Individual','Individual'),('Empresarial','Empresarial'))
estadoCliente = (('Inscrito','Inscrito'),('Matriculado','Matriculado'))


# En este modelo se agrega el contenido principal de la plataforma
# Entre ellos esta, Mision, Vision y Quienes Somos
class Contenido(models.Model):
	titulo = models.CharField(max_length=100, primary_key=True, help_text='Por favor,No edite este titulo')
	Contenido = models.TextField(help_text='Agregue el Contenido')

	def __unicode__(self):
		return self.titulo



# Este modelo contiene los datos de contacto de la Empresa
# Estos datos son mostrados en la seccion Contactame y en el pie de pagina de cada seccion
class Contacto(models.Model):
	Empresa = models.CharField(max_length=100, primary_key=True, help_text='Nombre de la Empresa')
	Pais = models.CharField(max_length=100, choices=pais)
	Ciudad = models.CharField(max_length=100)
	Telefono = models.CharField(max_length=50)
	Email = models.EmailField(help_text='correo@example.com')

	def __unicode__(self):
		return self.Empresa



# Modelo para definir los horarios de los cursos
class Horario(models.Model):
	Dia = models.CharField(max_length=40, choices = dias)
	De = models.CharField(max_length=40,help_text='Escribe la hora ej: 2:00 p.m.')
	Hasta = models.CharField(max_length=40,help_text='Escribe la hora ej: 2:00 p.m.')

	def __unicode__(self):
		return self.Dia + " " + self.De + " a " + self.Hasta



# Modelo para especificar el nombre y la descripcion del Facilitador de un curso
class Facilitador(models.Model):
	Nombre = models.CharField(max_length=100, unique=True)
<<<<<<< HEAD
	Descripcion = models.TextField(blank=True, help_text='Describa al Facilitador')
=======
	Descripcion = models.TextField(blank=True)
>>>>>>> 2bf9751ccd57ebab02aace68288197b0532a6702

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

<<<<<<< HEAD
# Este es el modelo inicial de cliente (Todavia es suceptible a modificaciones)
class Cliente(models.Model):
	Estado = models.CharField(choices = estadoCliente, max_length=50)
	Potencial = models.BooleanField(help_text='Es cliente potencial?')



# modelo para guardar los clientes que se han inscrito en alguno de los cursos ofertados
class Inscrito(models.Model):
	cliente = models.ForeignKey(Cliente, help_text='Escoja un cliente de la lista')
	fechaInscripcion = models.DateTimeField(auto_now_add=True)



# modelo para guardar los clientes que se han matriculado en alguno de los cursos ofertados
class Matriculado(models.Model):
	cliente = models.ForeignKey(Cliente, help_text='Escoja un cliente de la lista')
	fechaMatricula = models.DateTimeField(auto_now_add=True)



# Modelo del curso
=======
class Inscrito(models.Model):
	cliente = models.ForeignKey(Cliente)
	fechaInscripcion = models.DateTimeField(auto_now_add=True)

class Matriculado(models.Model):
	cliente = models.ForeignKey(Cliente)
	fechaMatricula = models.DateTimeField(auto_now_add=True)

>>>>>>> 2bf9751ccd57ebab02aace68288197b0532a6702
class Curso(models.Model):
	Nombre = models.CharField(max_length=100, unique=True, help_text='Nombre de Curso', null=False)
	Generalidades = models.TextField()
	Objetivos = models.TextField(help_text='Escriba cada objetivo separado por un salto de linea, si es subindice, agregue un guion')
	Duracion = models.IntegerField(help_text="Horas. Ej: 12")
	Horario = models.ManyToManyField(Horario, help_text='Asigne uno o varios horarios')
	Metodologia = models.TextField()
	Estado = models.CharField(choices= EstadoCurso, max_length=50)
<<<<<<< HEAD
	CupoMin = models.IntegerField(default=20)
	CupoMax = models.IntegerField(default=30)
	Inscritos = models.ManyToManyField(Inscrito, editable=False, blank=True)
	Matriculados = models.ManyToManyField(Matriculado, editable=False, blank=True)
	InicioInscripciones = models.DateField(auto_now=True, help_text='Feha Inicial Para Inscripciones')
	FinalInscripciones = models.DateField(help_text='Fecha Final para Inscripciones (La fecha de Inicio empieza al crear este curso)')
	FechaInicio = models.DateField(help_text='Fecha de Inicio de curso')
	FechaFinal = models.DateField(help_text='Fecha de Finalizacion de curso')
=======
	CupoMin = models.IntegerField()
	CupoMax = models.IntegerField()
	Inscritos = models.ManyToManyField(Inscrito, editable=False, blank=True)
	Matriculados = models.ManyToManyField(Matriculado, editable=False, blank=True)

	class Admin:
		list_display = ('Nombre', 'Duracion', 'Estado')
		list_filter = ('Duracion', 'Estado')
		ordering = ('-Estado',)
		search_fields = ('Nombre',)
>>>>>>> 2bf9751ccd57ebab02aace68288197b0532a6702

	def __unicode__(self):
		return self.Nombre

class Modulo(models.Model):
<<<<<<< HEAD
	Numero = models.IntegerField(help_text='Numero del modulo del curso')
	Nombre = models.CharField(max_length=150, unique=True, help_text='Nombre del modulo')
	Duracion = models.IntegerField(help_text='Ingrese un entero con el valor de las horas de duracion ej: 25')
	Facilitador = models.ForeignKey(Facilitador,null=True, help_text='Escoja un facilitador')
	Contenido = models.TextField(help_text='Ingrese el contenido separando cada apartado con un salto de linea')
	Curso = models.ForeignKey(Curso, help_text='Escoje el curso al cual pertenece este modulo')

	def __unicode__(self):
		return self.Nombre


# Los modelos de Usuario Individual y Empresarial son iniciales y no se han optimizado
# Esta tarea se hara en el segundo release
=======
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

>>>>>>> 2bf9751ccd57ebab02aace68288197b0532a6702

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