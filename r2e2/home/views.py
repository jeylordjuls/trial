from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from home.models import Requests

@login_required
def add_request(request):
	context = RequestContext(request)
	
	profile = UserProfile.objects.get(user=request.user)
	context_dict = {'profile': profile}

	if request.method == 'POST':
		event_name = request.POST['event']
		event.eventName = event_name
		event.save()
		
		return HttpResponseRedirect('/home/reservation_lists1/')

	else:
		return render_to_response('home/request_form.html', context_dict, context)

@login_required
def request_detail(request, reserve_id):
	context = RequestContext(request)
	# requests = Requests.objects.get(id=reserve_id)
	reserve = Requests.objects.get(id=reserve_id)

	profile = UserProfile.objects.get(user=request.user)
	context_dict = {'profile': profile, 'reserve': reserve}

	if request.method == 'POST':
		decision = request.POST['submit']
		if decision == 'APPROVE':
			reserve.tag = 1
			reserve.save()
		else:
			reserve.tag = 2
			reserve.save()
		return reservation_list(request)

	else:
		return render_to_response('home/request_details.html', context_dict, context)

@login_required
def reservation_list(request):
	context = RequestContext(request)

	requests = Requests.objects.all()

	profile = UserProfile.objects.get(user=request.user)
	context_dict = {'profile': profile, 'requests': requests}

	return render_to_response('home/reservation_lists.html', context_dict, context)

@login_required
def reservation_list1(request):
	context = RequestContext(request)

	requests = Requests.objects.filter(requestedBy=request.user)

	profile = UserProfile.objects.get(user=request.user)
	context_dict = {'profile': profile, 'requests': requests}

	return render_to_response('home/reservation_lists1.html', context_dict, context)

@login_required
def user_list(request):
	context = RequestContext(request)

	requests = Requests.objects.all()

	profile = UserProfile.objects.get(user=request.user)
	alluser = UserProfile.objects.all()
	context_dict = {'profile': profile, 'requests': requests, 'alluser': alluser,}

	return render_to_response('home/user_lists.html', context_dict, context)

