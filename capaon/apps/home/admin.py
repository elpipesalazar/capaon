from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from capaon.apps.home.models import Cliente,DatosEmpresa, Contacto, Horario, Facilitador, Modulo, Curso, Empresa, Inscrito, Matriculado, PerfilCliente


class AdminFacilitador(admin.ModelAdmin):
	list_filter = ('nombre',)
	ordering = ('-nombre',)
	search_fields = ('nombre',)

class ModuloInline(admin.TabularInline):
	model = Modulo

class AdminCurso(admin.ModelAdmin):
	list_display = ('nombre', 'duracion','estado')
	list_filter = ('duracion', 'estado')
	ordering = ('-estado',)
	search_fields = ('nombre',)
	inlines = [ModuloInline,]

class AdminModulo(admin.ModelAdmin):
	list_display = ('numero', 'nombre', 'facilitador','curso')
	list_filter = ['facilitador__nombre','curso__nombre']
	list_display_links = ('curso','nombre','facilitador')
	ordering = ('curso','numero')
	search_fields = ('nombre',)

class AdminHorario(admin.ModelAdmin):
	list_display = ('dia','de','hasta')

class ClienteProfileInline(admin.StackedInline):
    model = PerfilCliente
    can_delete = False
    verbose_name_plural = 'Cliente'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ClienteProfileInline, )


class EmpresaInline(admin.StackedInline):
	model = Empresa
	can_delete = False
	verbose_name_plural = 'Representante Legal'


class AdminPerfilCliente(admin.ModelAdmin):
	list_display = ('nombre', 'apellidos','user')
	list_filter = ('user__first_name',)

class AdminCliente(admin.ModelAdmin):
	list_display = ('perfil', 'tipo', 'potencial')
	list_filter = ('tipo','potencial')
	exclude = ('perfil', 'tipo')
	ordering = ('perfil__nombre',)
	can_delete = False

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(DatosEmpresa)
admin.site.register(Contacto)
admin.site.register(Horario, AdminHorario)
admin.site.register(Facilitador, AdminFacilitador)
#admin.site.register(Modulo, AdminModulo)
admin.site.register(Curso, AdminCurso)
admin.site.register(Empresa)
admin.site.register(Inscrito)
admin.site.register(Matriculado)
admin.site.register(PerfilCliente, AdminPerfilCliente)
admin.site.register(Cliente, AdminCliente)