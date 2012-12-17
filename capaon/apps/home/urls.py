from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('capaon.apps.home.views',
	url(r'^$','index_view', name='vistaInicial'),
	url(r'^register/$','register_view', name = 'vista_registro'),
	url(r'^register/empresa$','registrar_empresa', name = 'vista_registro_empresa'),
	url(r'^register/individual$','registrar_individual', name = 'vista_registro_individual'),
	url(r'^MisionVision/$','mv_view', name = 'vista_MisionVision'),
	url(r'^capacitacion/$','cursos_view', name = 'vista_Cursos'),
	url(r'^capacitacion/(\d{1,2})$','Infocursos_view', name = 'vista_InfoCursos'),
	url(r'^capacitacion/(\d{1,2})/inscripcion$','inscripcion_view', name = 'vista_inscripcion'),
	url(r'^contacto/$','contact_view', name = 'vista_Contacto'),
	url(r'^search/$','search_view', name = 'vista_search'),
	url(r'^login/$','login_view', name = 'login'),
	url(r'^logout/$','logout_view', name = 'logout'),
	url(r'^miscursos/$','miscursos_view', name = 'miscursos'),
	url(r'^profile/$','profile_view', name = 'vista_perfil'),
	)