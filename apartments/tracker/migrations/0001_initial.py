# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pro'
        db.create_table(u'tracker_pro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'tracker', ['Pro'])

        # Adding model 'Con'
        db.create_table(u'tracker_con', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'tracker', ['Con'])

        # Adding model 'Apartment'
        db.create_table(u'tracker_apartment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('photo', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('date_viewed', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('bedrooms', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('bathrooms', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=1)),
            ('sqft', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('rent', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('broker_multiplier', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2)),
            ('broker_fee', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('security_multiplier', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2)),
            ('security_fee', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=9, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=9, blank=True)),
        ))
        db.send_create_signal(u'tracker', ['Apartment'])

        # Adding M2M table for field pros on 'Apartment'
        db.create_table(u'tracker_apartment_pros', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apartment', models.ForeignKey(orm[u'tracker.apartment'], null=False)),
            ('pro', models.ForeignKey(orm[u'tracker.pro'], null=False))
        ))
        db.create_unique(u'tracker_apartment_pros', ['apartment_id', 'pro_id'])

        # Adding M2M table for field cons on 'Apartment'
        db.create_table(u'tracker_apartment_cons', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apartment', models.ForeignKey(orm[u'tracker.apartment'], null=False)),
            ('con', models.ForeignKey(orm[u'tracker.con'], null=False))
        ))
        db.create_unique(u'tracker_apartment_cons', ['apartment_id', 'con_id'])


    def backwards(self, orm):
        # Deleting model 'Pro'
        db.delete_table(u'tracker_pro')

        # Deleting model 'Con'
        db.delete_table(u'tracker_con')

        # Deleting model 'Apartment'
        db.delete_table(u'tracker_apartment')

        # Removing M2M table for field pros on 'Apartment'
        db.delete_table('tracker_apartment_pros')

        # Removing M2M table for field cons on 'Apartment'
        db.delete_table('tracker_apartment_cons')


    models = {
        u'tracker.apartment': {
            'Meta': {'object_name': 'Apartment'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'bathrooms': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'bedrooms': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'broker_fee': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'broker_multiplier': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '2'}),
            'cons': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tracker.Con']", 'symmetrical': 'False'}),
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_viewed': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '9', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '9', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'pros': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tracker.Pro']", 'symmetrical': 'False'}),
            'rent': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'security_fee': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'security_multiplier': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '2'}),
            'sqft': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'tracker.con': {
            'Meta': {'object_name': 'Con'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'tracker.pro': {
            'Meta': {'object_name': 'Pro'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['tracker']