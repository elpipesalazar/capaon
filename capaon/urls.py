from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    #Se conecta con las url de la aplicacion home para mostrar la pagina inicial
    url(r'^',include('capaon.apps.home.urls')),
    #activar servidor de medios en carpeta media
    url(r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),

    # Administrador Django
    # administrar:
    url(r'^admin/', include(admin.site.urls)),

)
