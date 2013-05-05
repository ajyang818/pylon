# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'tweet_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('screen_name', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('author_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('author_created', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('author_description', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal(u'tweet', ['Author'])

        # Adding model 'Hashtag'
        db.create_table(u'tweet_hashtag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hashtag', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'tweet', ['Hashtag'])

        # Adding model 'Tweet'
        db.create_table(u'tweet_tweet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tweet.Author'])),
            ('tweet_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('coordinates', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('user_mentions', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'tweet', ['Tweet'])

        # Adding M2M table for field hashtags on 'Tweet'
        db.create_table(u'tweet_tweet_hashtags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tweet', models.ForeignKey(orm[u'tweet.tweet'], null=False)),
            ('hashtag', models.ForeignKey(orm[u'tweet.hashtag'], null=False))
        ))
        db.create_unique(u'tweet_tweet_hashtags', ['tweet_id', 'hashtag_id'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'tweet_author')

        # Deleting model 'Hashtag'
        db.delete_table(u'tweet_hashtag')

        # Deleting model 'Tweet'
        db.delete_table(u'tweet_tweet')

        # Removing M2M table for field hashtags on 'Tweet'
        db.delete_table('tweet_tweet_hashtags')


    models = {
        u'tweet.author': {
            'Meta': {'object_name': 'Author'},
            'author_created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'author_description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'author_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'author_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        },
        u'tweet.hashtag': {
            'Meta': {'object_name': 'Hashtag'},
            'hashtag': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'tweet.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'author_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tweet.Author']"}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'coordinates': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'hashtags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tweet.Hashtag']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tweet_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'user_mentions': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tweet']