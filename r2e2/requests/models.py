from django.db import models
from events import Events
from schedules import Schedules
from rooms import Rooms
from accounts import CustomUser

# Create your models here.
class Requests(models.Model):
	event = models.ForeignKey(Events)
	schedule = models.ForeignKey(Schedules)
	room = models.ForeignKey(Rooms)
	requestedBy = models.ForeignKey(CustomUser)
	adminApproved = models.ForeignKey(CustomUser)
	chairApproves = models.ForeignKey(CustomUser)
