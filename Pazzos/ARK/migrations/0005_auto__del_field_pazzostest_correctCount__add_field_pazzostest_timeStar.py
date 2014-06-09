# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PazzosTest.correctCount'
        db.delete_column('ARK_pazzostest', 'correctCount')

        # Adding field 'PazzosTest.timeStarted'
        db.add_column('ARK_pazzostest', 'timeStarted',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.time(9, 43, 51, 510038)),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'PazzosTest.correctCount'
        db.add_column('ARK_pazzostest', 'correctCount',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'PazzosTest.timeStarted'
        db.delete_column('ARK_pazzostest', 'timeStarted')


    models = {
        'ARK.pazzostest': {
            'Meta': {'object_name': 'PazzosTest'},
            'correct_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ARK.PazzosTestWord']", 'symmetrical': 'False', 'related_name': "'pazzostest_correct_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'takenBy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ARK.PazzosUser']"}),
            'timeCompleted': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(9, 43, 51, 510038)'}),
            'timeStarted': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(9, 43, 51, 510038)'}),
            'word_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ARK.PazzosTestWord']", 'symmetrical': 'False', 'related_name': "'pazzostest_word_set'"})
        },
        'ARK.pazzostestword': {
            'Meta': {'object_name': 'PazzosTestWord'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'unique': 'True'}),
            'wordLength': ('django.db.models.fields.IntegerField', [], {})
        },
        'ARK.pazzosuser': {
            'Meta': {'object_name': 'PazzosUser'},
            'age': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'max_length': '255', 'unique': 'True'}),
            'english_level': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True'}),
            'handedness': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'db_table': "'django_content_type'", 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ARK']