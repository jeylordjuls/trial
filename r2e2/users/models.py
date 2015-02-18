from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	O = 'Organization'
	F = 'Faculty'
	G = 'Guest'
	SA = 'System Administrator'
	BA = 'Building Administrator'
	DC = 'Deparment Chair'

	User_Type_Choices = (
		(O, 'Organization'),
		(F, 'Faculty'),
		(G, 'Guest'),
		(SA, 'System Admin'),
		(BA, 'Building Admin'),
		(DC, 'Dept Chair'),
	)
	
	userType = models.CharField(max_length=20, choices=User_Type_Choices, default='SA')
	priorityLevel = models.IntegerField(default=0)
	additionalProperties = models.CharField(max_length=40)

	def __unicode__(self):
		return self.user.username
