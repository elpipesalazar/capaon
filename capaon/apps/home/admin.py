from django.contrib import admin
from capaon.apps.home.models import Contenido, Contacto, Horario, Facilitador, Modulo, Curso, Empresa, Individual, Inscrito, Matriculado
<<<<<<< HEAD

class AdminFacilitador(admin.ModelAdmin):
	list_filter = ('Nombre',)
	ordering = ('-Nombre',)
	search_fields = ('Nombre',)

class ModuloInline(admin.TabularInline):
	model = Modulo

class AdminCurso(admin.ModelAdmin):
	list_display = ('Nombre', 'Duracion','Estado')
	list_filter = ('Duracion', 'Estado')
	ordering = ('-Estado',)
	search_fields = ('Nombre',)
	inlines = [ModuloInline,]

class AdminModulo(admin.ModelAdmin):
	list_display = ('Numero', 'Nombre', 'Facilitador','Curso')
	list_filter = ('Facilitador', 'Curso__Nombre',)
	list_display_links = ('Curso','Nombre','Facilitador')
	ordering = ('Curso','Numero')
	search_fields = ('Nombre',)

class AdminHorario(admin.ModelAdmin):
	list_display = ('Dia','De','Hasta')

=======
>>>>>>> 2bf9751ccd57ebab02aace68288197b0532a6702

admin.site.register(Contenido)
admin.site.register(Contacto)
admin.site.register(Horario, AdminHorario)
admin.site.register(Facilitador, AdminFacilitador)
admin.site.register(Modulo, AdminModulo)
admin.site.register(Curso, AdminCurso)
admin.site.register(Empresa)
admin.site.register(Individual)
admin.site.register(Inscrito)
admin.site.register(Matriculado)