from django.db import models

class Meet(models.Model):
  place = models.CharField(max_length=200)
  date = models.CharField(max_length=200)
  sender = models.CharField(max_length=200)
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
  sender = models.CharField(max_length = 200)
  def __unicode__(self):
    return self.comment
