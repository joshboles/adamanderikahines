# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'DinnerChoice'
        db.create_table('rsvp_dinnerchoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('rsvp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rsvp.Rsvp'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('dinner_choice', self.gf('django.db.models.fields.CharField')(default='turkey', max_length=16)),
        ))
        db.send_create_signal('rsvp', ['DinnerChoice'])

        # Deleting field 'Rsvp.stuffed_turkey_roulade'
        db.delete_column('rsvp_rsvp', 'stuffed_turkey_roulade')

        # Deleting field 'Rsvp.citrus_grilled_salmon'
        db.delete_column('rsvp_rsvp', 'citrus_grilled_salmon')

        # Deleting field 'Rsvp.names'
        db.delete_column('rsvp_rsvp', 'names')

        # Deleting field 'Rsvp.how_many'
        db.delete_column('rsvp_rsvp', 'how_many')

        # Adding field 'Rsvp.email'
        db.add_column('rsvp_rsvp', 'email', self.gf('django.db.models.fields.EmailField')(default=' ', max_length=75), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'DinnerChoice'
        db.delete_table('rsvp_dinnerchoice')

        # Adding field 'Rsvp.stuffed_turkey_roulade'
        db.add_column('rsvp_rsvp', 'stuffed_turkey_roulade', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Rsvp.citrus_grilled_salmon'
        db.add_column('rsvp_rsvp', 'citrus_grilled_salmon', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Rsvp.names'
        db.add_column('rsvp_rsvp', 'names', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True), keep_default=False)

        # Adding field 'Rsvp.how_many'
        db.add_column('rsvp_rsvp', 'how_many', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Deleting field 'Rsvp.email'
        db.delete_column('rsvp_rsvp', 'email')


    models = {
        'rsvp.dinnerchoice': {
            'Meta': {'object_name': 'DinnerChoice'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'dinner_choice': ('django.db.models.fields.CharField', [], {'default': "'turkey'", 'max_length': '16'}),
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
