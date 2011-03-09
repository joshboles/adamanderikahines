# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'DinnerChoice.dinner_choice'
        db.alter_column('rsvp_dinnerchoice', 'dinner_choice', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))


    def backwards(self, orm):
        
        # Changing field 'DinnerChoice.dinner_choice'
        db.alter_column('rsvp_dinnerchoice', 'dinner_choice', self.gf('django.db.models.fields.CharField')(max_length=16))


    models = {
        'rsvp.dinnerchoice': {
            'Meta': {'object_name': 'DinnerChoice'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'dinner_choice': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '16', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'rsvp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rsvp.Rsvp']"})
        },
        'rsvp.rsvp': {
            'Meta': {'object_name': 'Rsvp'},
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'dinner_dancing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['rsvp']
