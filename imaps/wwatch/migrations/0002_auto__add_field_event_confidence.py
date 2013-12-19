# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.confidence'
        db.add_column(u'wwatch_event', 'confidence',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.confidence'
        db.delete_column(u'wwatch_event', 'confidence')


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
            'confidence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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