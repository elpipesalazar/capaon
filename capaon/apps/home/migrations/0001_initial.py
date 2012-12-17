# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DatosEmpresa'
        db.create_table('home_datosempresa', (
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('Contenido', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('home', ['DatosEmpresa'])

        # Adding model 'Contacto'
        db.create_table('home_contacto', (
            ('empresa', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('home', ['Contacto'])

        # Adding model 'Horario'
        db.create_table('home_horario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dia', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('de', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('hasta', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('home', ['Horario'])

        # Adding model 'Facilitador'
        db.create_table('home_facilitador', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('home', ['Facilitador'])

        # Adding model 'Curso'
        db.create_table('home_curso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('generalidades', self.gf('django.db.models.fields.TextField')()),
            ('objetivos', self.gf('django.db.models.fields.TextField')()),
            ('duracion', self.gf('django.db.models.fields.IntegerField')()),
            ('metodologia', self.gf('django.db.models.fields.TextField')()),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('cupoMin', self.gf('django.db.models.fields.IntegerField')(default=20)),
            ('cupoMax', self.gf('django.db.models.fields.IntegerField')(default=30)),
            ('inicioInscripciones', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('finalInscripciones', self.gf('django.db.models.fields.DateField')()),
            ('fechaInicio', self.gf('django.db.models.fields.DateField')()),
            ('fechaFinal', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('home', ['Curso'])

        # Adding M2M table for field horario on 'Curso'
        db.create_table('home_curso_horario', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('curso', models.ForeignKey(orm['home.curso'], null=False)),
            ('horario', models.ForeignKey(orm['home.horario'], null=False))
        ))
        db.create_unique('home_curso_horario', ['curso_id', 'horario_id'])

        # Adding model 'Inscrito'
        db.create_table('home_inscrito', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('curso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Curso'], null=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('fechaInscripcion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('FechaCaducidad', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('home', ['Inscrito'])

        # Adding model 'Matriculado'
        db.create_table('home_matriculado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('curso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Curso'], null=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('fechaMatricula', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('home', ['Matriculado'])

        # Adding model 'Modulo'
        db.create_table('home_modulo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('duracion', self.gf('django.db.models.fields.IntegerField')()),
            ('facilitador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Facilitador'], null=True)),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('curso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Curso'])),
        ))
        db.send_create_signal('home', ['Modulo'])

        # Adding model 'PerfilCliente'
        db.create_table('home_perfilcliente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='perfil', unique=True, to=orm['auth.User'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('cedula', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fechaNacimiento', self.gf('django.db.models.fields.DateField')(null=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('home', ['PerfilCliente'])

        # Adding model 'Empresa'
        db.create_table('home_empresa', (
            ('razonSocial', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nit', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('actividad', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('representante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.PerfilCliente'], unique=True)),
        ))
        db.send_create_signal('home', ['Empresa'])

        # Adding model 'Cliente'
        db.create_table('home_cliente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('perfil', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.PerfilCliente'], unique=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('potencial', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('home', ['Cliente'])


    def backwards(self, orm):
        # Deleting model 'DatosEmpresa'
        db.delete_table('home_datosempresa')

        # Deleting model 'Contacto'
        db.delete_table('home_contacto')

        # Deleting model 'Horario'
        db.delete_table('home_horario')

        # Deleting model 'Facilitador'
        db.delete_table('home_facilitador')

        # Deleting model 'Curso'
        db.delete_table('home_curso')

        # Removing M2M table for field horario on 'Curso'
        db.delete_table('home_curso_horario')

        # Deleting model 'Inscrito'
        db.delete_table('home_inscrito')

        # Deleting model 'Matriculado'
        db.delete_table('home_matriculado')

        # Deleting model 'Modulo'
        db.delete_table('home_modulo')

        # Deleting model 'PerfilCliente'
        db.delete_table('home_perfilcliente')

        # Deleting model 'Empresa'
        db.delete_table('home_empresa')

        # Deleting model 'Cliente'
        db.delete_table('home_cliente')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'home.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perfil': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.PerfilCliente']", 'unique': 'True'}),
            'potencial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'home.contacto': {
            'Meta': {'object_name': 'Contacto'},
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'empresa': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'home.curso': {
            'Meta': {'object_name': 'Curso'},
            'cupoMax': ('django.db.models.fields.IntegerField', [], {'default': '30'}),
            'cupoMin': ('django.db.models.fields.IntegerField', [], {'default': '20'}),
            'duracion': ('django.db.models.fields.IntegerField', [], {}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'fechaFinal': ('django.db.models.fields.DateField', [], {}),
            'fechaInicio': ('django.db.models.fields.DateField', [], {}),
            'finalInscripciones': ('django.db.models.fields.DateField', [], {}),
            'generalidades': ('django.db.models.fields.TextField', [], {}),
            'horario': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['home.Horario']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicioInscripciones': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'metodologia': ('django.db.models.fields.TextField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'objetivos': ('django.db.models.fields.TextField', [], {})
        },
        'home.datosempresa': {
            'Contenido': ('django.db.models.fields.TextField', [], {}),
            'Meta': {'object_name': 'DatosEmpresa'},
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'})
        },
        'home.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'actividad': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nit': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'razonSocial': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'representante': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.PerfilCliente']", 'unique': 'True'})
        },
        'home.facilitador': {
            'Meta': {'object_name': 'Facilitador'},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'home.horario': {
            'Meta': {'object_name': 'Horario'},
            'de': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'dia': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'hasta': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'home.inscrito': {
            'FechaCaducidad': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'Meta': {'object_name': 'Inscrito'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Curso']", 'null': 'True'}),
            'fechaInscripcion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'home.matriculado': {
            'Meta': {'object_name': 'Matriculado'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Curso']", 'null': 'True'}),
            'fechaMatricula': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'home.modulo': {
            'Meta': {'object_name': 'Modulo'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Curso']"}),
            'duracion': ('django.db.models.fields.IntegerField', [], {}),
            'facilitador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Facilitador']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'numero': ('django.db.models.fields.IntegerField', [], {})
        },
        'home.perfilcliente': {
            'Meta': {'object_name': 'PerfilCliente'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fechaNacimiento': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'perfil'", 'unique': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['home']