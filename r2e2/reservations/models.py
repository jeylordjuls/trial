from django.db import models
from django.contrib.admin.widgets import AdminTimeWidget
from users.models import UserProfile
from rooms.models import Rooms
# Create your models here.

class Requests(models.Model):
	#event = models.ForeignKey(Events)
	#schedule = models.ForeignKey(Schedules)
	eventName = models.CharField(max_length=30,null=True, blank=True)
	# eventType = models.CharField(max_length=30,null=True, blank=True)
	partiNumber = models.IntegerField(null=True, blank=True)
	room = models.ForeignKey(Rooms)
	startTime = models.TimeField(null=True, blank=True)
	endTime = models.TimeField(null=True, blank=True)
	date = models.DateField(null=True, blank=True)
	purpose = models.CharField(max_length=50,null=True, blank=True)
	requestedBy = models.ForeignKey(UserProfile, related_name='requests_requestedBy',null=True, blank=True)
	approvedBy = models.ForeignKey(UserProfile,related_name='requests_adminApproved',null=True, blank=True)
	tag = models.IntegerField(null=True, blank=True)
	# user_type = models.ForeignKey(UserProfile,null=True,blank=True)
	# req = models.CharField(max_length=50,null=True, blank=True)
	#adminApproved = models.ForeignKey(UserProfile, related_name='requests_adminApproved')
	#chairApproves = models.ForeignKey(UserProfile, related_name='requests_chairApproves')
 
	def __unicode__(self):
		return self.eventName

	class Meta:
		verbose_name_plural = 'Requests'