from django.db import models
from schedules.models import Schedules

# Create your models here.
class Rooms(models.Model):
	roomName = models.CharField(max_length=20)
	roomType = models.CharField(max_length=20)
	roomNumber = models.IntegerField()
	capacity = models.IntegerField()
	schedules = models.ForeignKey(Schedules)

	def __unicode__(self):
        	return self.roomName
	class Meta:
		verbose_name_plural = 'Schedules'
