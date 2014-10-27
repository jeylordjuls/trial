from django.db import models
from events.models import Events

# Create your models here.
class Schedules(models.Model):
	startTime = models.TimeField()
	endTime = models.TimeField()
	date = models.DateField()
	event = models.ForeignKey(Events)

	def __unicode__(self):
        	return self.eventName
	class Meta:
		verbose_name_plural = 'Schedules'