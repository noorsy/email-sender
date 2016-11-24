from django.db import models

# Create your models here.
class uploadData(models.Model):
	name = models.CharField(max_length=20, null=True, blank=True)
	link = models.CharField(max_length=20, null=True, blank=True)
	email = models.CharField(max_length=20, null=True, blank=True)
	def __unicode__(self):
		return unicode(self.name) or u''



class testModel(models.Model):
	name = models.CharField(max_length=20, null=True, blank=True)
	def __unicode__(self):
		return self.name