from django.contrib import admin
from capaon.apps.home.models import Contenido, Empresa, Curso, Contacto

admin.site.register(Contenido)
admin.site.register(Empresa)
admin.site.register(Curso)
admin.site.register(Contacto)
