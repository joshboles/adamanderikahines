# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Rsvp'
        db.create_table('rsvp_rsvp', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('dinner_dancing', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('how_many', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('names', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('stuffed_turkey_roulade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('citrus_grilled_salmon', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('rsvp', ['Rsvp'])


    def backwards(self, orm):
        
        # Deleting model 'Rsvp'
        db.delete_table('rsvp_rsvp')


    models = {
        'rsvp.rsvp': {
            'Meta': {'object_name': 'Rsvp'},
            'citrus_grilled_salmon': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'dinner_dancing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'how_many': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'names': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'stuffed_turkey_roulade': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['rsvp']
