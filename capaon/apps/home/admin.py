from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from capaon.apps.home.models import Contenido, Contacto, Horario, Facilitador, Modulo, Curso, Empresa, Inscrito, Matriculado, PerfilCliente


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

class ClienteProfileInline(admin.StackedInline):
    model = PerfilCliente
    can_delete = False
    verbose_name_plural = 'Cliente'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ClienteProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Contenido)
admin.site.register(Contacto)
admin.site.register(Horario, AdminHorario)
admin.site.register(Facilitador, AdminFacilitador)
admin.site.register(Modulo, AdminModulo)
admin.site.register(Curso, AdminCurso)
admin.site.register(Empresa)
admin.site.register(Inscrito)
admin.site.register(Matriculado)
admin.site.register(PerfilCliente)