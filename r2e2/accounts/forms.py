from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile
from home.models import Requests,Rooms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('additionalProperties','userType',)


#class EventForm(forms.ModelForm):

   # class Meta:
	#model = Events
	#fields = ('eventName', 'eventType',)

class RoomForm(forms.ModelForm):
	
    class Meta:
		model = Rooms
		fields = ('roomName','roomNumber')

class ReserveForm(forms.ModelForm):

    	class Meta:
			model = Requests
			fields = ('eventName','partiNumber','room','startTime','endTime','date','purpose')


		
#class ScheduleForm(forms.ModelForm):

    #class Meta:
	#model = Schedules
	#fields = ('startTime', 'endTime', 'date',)
	
