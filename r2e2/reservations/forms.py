from django.http import HttpResponseRedirect
from django import forms
from reservations.models import Requests



class ReserveForm(forms.ModelForm):

    	class Meta:
			model = Requests
			fields = ('eventName','partiNumber','room','startTime','endTime','date','purpose')