from django.db import models
from django.contrib.auth.models import User

class Meet(models.Model):
  place = models.CharField(max_length=200)
  date = models.DateField('date')
  sender = models.ForeignKey(User)
  def __unicode__(self):
    return self.place

class Choice(models.Model):
  meet = models.ForeignKey(Meet)
  choice = models.CharField(max_length = 200)
  vote = models.IntegerField()
  def __unicode__(self):
    return self.choice

class Comment(models.Model):
  meet = models.ForeignKey(Meet)
  comment = models.CharField(max_length = 200)
  sender = models.ForeignKey(User)
  def __unicode__(self):
    return self.comment
