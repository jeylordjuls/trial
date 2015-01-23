from django.db import models
from accounts.models import UserProfile
from django.contrib.admin.widgets import AdminTimeWidget
# Create your models here.
class Rooms(models.Model):
	roomName = models.CharField(max_length=20)
	roomType = models.CharField(max_length=20)
	roomNumber = models.IntegerField()
	#capacity = models.IntegerField()

	def __unicode__(self):
		return self.roomName

	class Meta:
		verbose_name_plural = 'Rooms'

#class Events(models.Model):
	#eventName = models.CharField(max_length=20)
	#eventType = models.CharField(max_length=20)
	#startTime = models.TimeField()
	#endTime = models.TimeField()
	#date = models.DateField()
	#created_by = models.ForeignKey(UserProfile, related_name='events_created_by')
	#created_by = models.CharField(max_length=30);
	#approved_by = models.ForeignKey(UserProfile, related_name='events_approved_by')
	#approvalStatus = models.CharField(max_length=30)

	#def __unicode__(self):
		#return self.eventName

	#class Meta:
		#verbose_name_plural = 'Events'

#class Schedules(models.Model):
	#startTime = models.TimeField()
	#endTime = models.TimeField()
	#date = models.DateField()
	#event = models.ForeignKey(Events)

	#class Meta:
		#verbose_name_plural = 'Schedules'

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


