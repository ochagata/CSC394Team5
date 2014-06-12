# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PazzosTest'
        db.create_table(u'ARK_pazzostest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('takenBy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ARK.PazzosUser'])),
            ('timeStarted', self.gf('django.db.models.fields.TimeField')(default=datetime.time(16, 16, 32, 40000))),
            ('timeCompleted', self.gf('django.db.models.fields.TimeField')(default=datetime.time(16, 16, 32, 40000))),
        ))
        db.send_create_signal(u'ARK', ['PazzosTest'])


    def backwards(self, orm):
        # Deleting model 'PazzosTest'
        db.delete_table(u'ARK_pazzostest')


    models = {
        u'ARK.pazzoskeyboard': {
            'Meta': {'object_name': 'PazzosKeyboard'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ARK.pazzostest': {
            'Meta': {'object_name': 'PazzosTest'},
            'correct_list': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'pazzostest_correct_set'", 'symmetrical': 'False', 'to': u"orm['ARK.PazzosTestWord']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'takenBy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ARK.PazzosUser']"}),
            'timeCompleted': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(16, 16, 32, 40000)'}),
            'timeStarted': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(16, 16, 32, 40000)'}),
            'word_list': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'pazzostest_word_set'", 'symmetrical': 'False', 'to': u"orm['ARK.PazzosTestWord']"})
        },
        u'ARK.pazzostestword': {
            'Meta': {'object_name': 'PazzosTestWord'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'wordLength': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ARK.pazzosuser': {
            'Meta': {'object_name': 'PazzosUser'},
            'age': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'english_level': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            'handedness': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ARK']