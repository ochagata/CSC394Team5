# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PazzosTestWord'
        db.create_table('ARK_pazzostestword', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, db_index=True)),
            ('wordLength', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('ARK', ['PazzosTestWord'])

        # Adding model 'PazzosTest'
        db.create_table('ARK_pazzostest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('takenBy', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ARK.PazzosUser'], unique=True)),
            ('timeCompleted', self.gf('django.db.models.fields.TimeField')()),
            ('correctCount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('ARK', ['PazzosTest'])

        # Adding M2M table for field word_list on 'PazzosTest'
        m2m_table_name = db.shorten_name('ARK_pazzostest_word_list')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pazzostest', models.ForeignKey(orm['ARK.pazzostest'], null=False)),
            ('pazzostestword', models.ForeignKey(orm['ARK.pazzostestword'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pazzostest_id', 'pazzostestword_id'])

        # Adding M2M table for field correct_list on 'PazzosTest'
        m2m_table_name = db.shorten_name('ARK_pazzostest_correct_list')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pazzostest', models.ForeignKey(orm['ARK.pazzostest'], null=False)),
            ('pazzostestword', models.ForeignKey(orm['ARK.pazzostestword'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pazzostest_id', 'pazzostestword_id'])


    def backwards(self, orm):
        # Deleting model 'PazzosTestWord'
        db.delete_table('ARK_pazzostestword')

        # Deleting model 'PazzosTest'
        db.delete_table('ARK_pazzostest')

        # Removing M2M table for field word_list on 'PazzosTest'
        db.delete_table(db.shorten_name('ARK_pazzostest_word_list'))

        # Removing M2M table for field correct_list on 'PazzosTest'
        db.delete_table(db.shorten_name('ARK_pazzostest_correct_list'))


    models = {
        'ARK.pazzostest': {
            'Meta': {'object_name': 'PazzosTest'},
            'correctCount': ('django.db.models.fields.IntegerField', [], {}),
            'correct_list': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'pazzostest_correct_set'", 'to': "orm['ARK.PazzosTestWord']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'takenBy': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['ARK.PazzosUser']", 'unique': 'True'}),
            'timeCompleted': ('django.db.models.fields.TimeField', [], {}),
            'word_list': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'pazzostest_word_set'", 'to': "orm['ARK.PazzosTestWord']", 'symmetrical': 'False'})
        },
        'ARK.pazzostestword': {
            'Meta': {'object_name': 'PazzosTestWord'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'db_index': 'True'}),
            'wordLength': ('django.db.models.fields.IntegerField', [], {})
        },
        'ARK.pazzosuser': {
            'Meta': {'object_name': 'PazzosUser'},
            'age': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'unique': 'True', 'db_index': 'True'}),
            'english_level': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'handedness': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ARK']