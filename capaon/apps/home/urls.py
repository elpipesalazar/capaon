from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('capaon.apps.home.views',
	url(r'^$','index_view', name='vistaInicial'),
	url(r'^register/$','construccion', name = 'vista_registro'),
	url(r'^QuienesSomos/$','about_view', name = 'vista_acerca'),
	url(r'^MisionVision/$','mv_view', name = 'vista_MisionVision'),
	url(r'^cursos/$','construccion', name = 'vista_Cursos'),
	url(r'^contacto/$','contact_view', name = 'vista_Contacto'),
	)