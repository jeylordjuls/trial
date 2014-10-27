from django.db import models
from django.contrib.auth.models import AbstractUser
 
class CustomUser(AbstractUser):
    pass
 
class Faculty(CustomUser):
 	priorityLevel = models.IntegerField(default=3, editable=False)
 	additionalProperties = models.TextField(max_length=150)
	
	class Meta:
		verbose_name = 'Faculty Member'

class Organization(CustomUser):
 	priorityLevel = models.IntegerField(default=4, editable=False)
 	additionalProperties = models.TextField(max_length=150)

	class Meta:
		verbose_name = 'Organization'

class Guest(CustomUser):
 	priorityLevel = models.IntegerField(default=5, editable=False)
 	additionalProperties = models.TextField(max_length=150)

	class Meta:
		verbose_name = 'Guest'

class BuildingAdmin(CustomUser):
 	priorityLevel = models.IntegerField(default=2, editable=False)
 	additionalProperties = models.TextField(max_length=150)

	class Meta:
		verbose_name = 'Building Administrator'

class DepartmentChair(CustomUser):
 	priorityLevel = models.IntegerField(default=1, editable=False)
 	additionalProperties = models.TextField(max_length=150)

	class Meta:
		verbose_name = 'Department Chair'

class Adviser(models.Model):
	faculty = models.ForeignKey(Faculty)
	organization = models.ForeignKey(Organization)
 
