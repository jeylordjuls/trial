from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Events(models.Model):
	eventName = models.CharField(max_length=30)
	eventType = models.CharField(max_length=20)
	timeStamp = models.DateField()
	created_by = models.ForeignKey(CustomUser, related_name='events_created_by')
	approved_by = models.ForeignKey(CustomUser, related_name='events_approved_by')
	approvalStatus = models.CharField(max_length=30)

	def __unicode__(self):
        	return self.eventName
	class Meta:
		verbose_name_plural = 'Events'