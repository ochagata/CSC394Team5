# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'PazzosTest', fields ['takenBy']
        db.delete_unique('ARK_pazzostest', ['takenBy_id'])


        # Changing field 'PazzosTest.takenBy'
        db.alter_column('ARK_pazzostest', 'takenBy_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ARK.PazzosUser']))

    def backwards(self, orm):

        # Changing field 'PazzosTest.takenBy'
        db.alter_column('ARK_pazzostest', 'takenBy_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['ARK.PazzosUser']))
        # Adding unique constraint on 'PazzosTest', fields ['takenBy']
        db.create_unique('ARK_pazzostest', ['takenBy_id'])


    models = {
        'ARK.pazzostest': {
            'Meta': {'object_name': 'PazzosTest'},
            'correctCount': ('django.db.models.fields.IntegerField', [], {}),
            'correct_list': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'pazzostest_correct_set'", 'to': "orm['ARK.PazzosTestWord']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'takenBy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ARK.PazzosUser']"}),
            'timeCompleted': ('django.db.models.fields.TimeField', [], {}),
            'word_list': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'pazzostest_word_set'", 'to': "orm['ARK.PazzosTestWord']", 'symmetrical': 'False'})
        },
        'ARK.pazzostestword': {
            'Meta': {'object_name': 'PazzosTestWord'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'wordLength': ('django.db.models.fields.IntegerField', [], {})
        },
        'ARK.pazzosuser': {
            'Meta': {'object_name': 'PazzosUser'},
            'age': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'english_level': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '1'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'gender': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '1'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False'}),
            'handedness': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ARK']