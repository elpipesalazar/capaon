# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Curso'
        db.create_table('home_curso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('NombreCurso', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('Generalidades', self.gf('django.db.models.fields.TextField')()),
            ('Objetivos', self.gf('django.db.models.fields.TextField')()),
            ('Duracion', self.gf('django.db.models.fields.IntegerField')()),
            ('Metodologia', self.gf('django.db.models.fields.TextField')()),
            ('Estado', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('CupoMin', self.gf('django.db.models.fields.IntegerField')(default=20)),
            ('CupoMax', self.gf('django.db.models.fields.IntegerField')(default=30)),
            ('InicioInscripciones', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('FinalInscripciones', self.gf('django.db.models.fields.DateField')()),
            ('FechaInicio', self.gf('django.db.models.fields.DateField')()),
            ('FechaFinal', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('home', ['Curso'])

        # Adding M2M table for field Horario on 'Curso'
        db.create_table('home_curso_Horario', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('curso', models.ForeignKey(orm['home.curso'], null=False)),
            ('horario', models.ForeignKey(orm['home.horario'], null=False))
        ))
        db.create_unique('home_curso_Horario', ['curso_id', 'horario_id'])

        # Adding M2M table for field Inscritos on 'Curso'
        db.create_table('home_curso_Inscritos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('curso', models.ForeignKey(orm['home.curso'], null=False)),
            ('inscrito', models.ForeignKey(orm['home.inscrito'], null=False))
        ))
        db.create_unique('home_curso_Inscritos', ['curso_id', 'inscrito_id'])

        # Adding M2M table for field Matriculados on 'Curso'
        db.create_table('home_curso_Matriculados', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('curso', models.ForeignKey(orm['home.curso'], null=False)),
            ('matriculado', models.ForeignKey(orm['home.matriculado'], null=False))
        ))
        db.create_unique('home_curso_Matriculados', ['curso_id', 'matriculado_id'])

        # Adding field 'Modulo.Curso'
        db.add_column('home_modulo', 'Curso',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['home.Curso']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Curso'
        db.delete_table('home_curso')

        # Removing M2M table for field Horario on 'Curso'
        db.delete_table('home_curso_Horario')

        # Removing M2M table for field Inscritos on 'Curso'
        db.delete_table('home_curso_Inscritos')

        # Removing M2M table for field Matriculados on 'Curso'
        db.delete_table('home_curso_Matriculados')

        # Deleting field 'Modulo.Curso'
        db.delete_column('home_modulo', 'Curso_id')


    models = {
        'home.cliente': {
            'Estado': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'object_name': 'Cliente'},
            'Potencial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'home.contacto': {
            'Ciudad': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'Empresa': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'Meta': {'object_name': 'Contacto'},
            'Pais': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Telefono': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'home.contenido': {
            'Contenido': ('django.db.models.fields.TextField', [], {}),
            'Meta': {'object_name': 'Contenido'},
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'})
        },
        'home.curso': {
            'CupoMax': ('django.db.models.fields.IntegerField', [], {'default': '30'}),
            'CupoMin': ('django.db.models.fields.IntegerField', [], {'default': '20'}),
            'Duracion': ('django.db.models.fields.IntegerField', [], {}),
            'Estado': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'FechaFinal': ('django.db.models.fields.DateField', [], {}),
            'FechaInicio': ('django.db.models.fields.DateField', [], {}),
            'FinalInscripciones': ('django.db.models.fields.DateField', [], {}),
            'Generalidades': ('django.db.models.fields.TextField', [], {}),
            'Horario': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['home.Horario']", 'symmetrical': 'False'}),
            'InicioInscripciones': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'Inscritos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['home.Inscrito']", 'symmetrical': 'False', 'blank': 'True'}),
            'Matriculados': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['home.Matriculado']", 'symmetrical': 'False', 'blank': 'True'}),
            'Meta': {'object_name': 'Curso'},
            'Metodologia': ('django.db.models.fields.TextField', [], {}),
            'NombreCurso': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'Objetivos': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'home.empresa': {
            'Actividad': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Direccion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'Email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'Fax': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Meta': {'object_name': 'Empresa'},
            'NIT': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'Pais': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'RazonSocial': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Telefono': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'home.facilitador': {
            'Descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'Meta': {'object_name': 'Facilitador'},
            'Nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'home.horario': {
            'De': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'Dia': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'Hasta': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'Meta': {'object_name': 'Horario'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'home.individual': {
            'Apellido': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Cedula': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Celular': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Direccion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'FechaNacimiento': ('django.db.models.fields.DateField', [], {}),
            'Meta': {'object_name': 'Individual'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Pais': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Telefono': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'home.inscrito': {
            'Meta': {'object_name': 'Inscrito'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Cliente']"}),
            'fechaInscripcion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'home.matriculado': {
            'Meta': {'object_name': 'Matriculado'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Cliente']"}),
            'fechaMatricula': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'home.modulo': {
            'Contenido': ('django.db.models.fields.TextField', [], {}),
            'Curso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Curso']"}),
            'Duracion': ('django.db.models.fields.IntegerField', [], {}),
            'Facilitador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Facilitador']", 'null': 'True'}),
            'Meta': {'object_name': 'Modulo'},
            'Nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'Numero': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['home']