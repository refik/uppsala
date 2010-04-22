from django.db import models
from django.contrib.auth.models import User

class shout(models.Model):
	shout = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published', auto_now_add = True)
	user = models.ForeignKey(User)
	def __unicode__(self):
		return u"%s: %s" % (self.user, self.shout,)

