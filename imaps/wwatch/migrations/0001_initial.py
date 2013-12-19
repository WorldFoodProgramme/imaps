# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Resource'
        db.create_table(u'wwatch_resource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('document', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wwatch.Event'])),
        ))
        db.send_create_signal(u'wwatch', ['Resource'])

        # Adding model 'Link'
        db.create_table(u'wwatch_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wwatch.Event'])),
        ))
        db.send_create_signal(u'wwatch', ['Link'])

        # Adding model 'Country'
        db.create_table(u'wwatch_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('iso_3', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('color_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('terr_id', self.gf('django.db.models.fields.IntegerField')()),
            ('terr_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('shape_leng', self.gf('django.db.models.fields.FloatField')()),
            ('shape_area', self.gf('django.db.models.fields.FloatField')()),
            ('mpoly', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal(u'wwatch', ['Country'])

        # Adding model 'Event'
        db.create_table(u'wwatch_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wwatch.Country'])),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('hazard_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('alert_level', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('event_comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'wwatch', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Resource'
        db.delete_table(u'wwatch_resource')

        # Deleting model 'Link'
        db.delete_table(u'wwatch_link')

        # Deleting model 'Country'
        db.delete_table(u'wwatch_country')

        # Deleting model 'Event'
        db.delete_table(u'wwatch_event')


    models = {
        u'wwatch.country': {
            'Meta': {'object_name': 'Country'},
            'color_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso_3': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mpoly': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'shape_area': ('django.db.models.fields.FloatField', [], {}),
            'shape_leng': ('django.db.models.fields.FloatField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'terr_id': ('django.db.models.fields.IntegerField', [], {}),
            'terr_name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'wwatch.event': {
            'Meta': {'object_name': 'Event'},
            'alert_level': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wwatch.Country']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'event_comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'hazard_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'wwatch.link': {
            'Meta': {'object_name': 'Link'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wwatch.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '255'})
        },
        u'wwatch.resource': {
            'Meta': {'object_name': 'Resource'},
            'document': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wwatch.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['wwatch']