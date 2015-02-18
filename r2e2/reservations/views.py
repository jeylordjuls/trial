from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.models import UserProfile
from reservations.forms import ReserveForm
from rooms.models import Rooms
from reservations.models import Requests

@login_required
def add_reserve(request):
    registered = False
    profile = UserProfile.objects.get(user=request.user)
    rooms = Rooms.objects.all()
    user = request.user
    if request.method == 'POST':
        #event_form = EventForm(data=request.POST)
	#room_form = RoomForm(data=request.POST)
	#schedule_form = ScheduleForm(data=request.POST)
	reserve_form = ReserveForm(data=request.POST)

        #if event_form.is_valid() and room_form.is_valid() and schedule_form.is_valid():
	if reserve_form.is_valid():
            reserve = reserve_form.save()
            reserve.requestedBy = profile
            reserve.tag = 0
            reserve.save()
	   # event.created_by = profile
	   # event.approvalStatus = "AA"
           # event.save()
	   # room = room_form.save()
	   # room.save()

	   # schedule = schedule_form.save()
	   # schedule.save()

            registered = True

            if user.is_superuser:

                return HttpResponseRedirect('/users/reservations/reservation_lists/')
            else:
                return HttpResponseRedirect('/users/reservations/reservation_lists1/')

        else:
	    print reserve_form.errors
            # print event_form.errors, room_form.errors, schedule_form.errors
    else:
        # event_form = EventForm()
        # room_form = RoomForm()
	# schedule_form = ScheduleForm()
	reserve_form = ReserveForm()

    return render(request,
            'reservations/reserve.html',
	     {'reserve_form': reserve_form,'registered':registered, 'rooms':rooms, 'profile':profile,})

@login_required
def add_request(request):
	context = RequestContext(request)
	
	profile = UserProfile.objects.get(user=request.user)
	context_dict = {'profile': profile}

	if request.method == 'POST':
		event_name = request.POST['event']
		event.eventName = event_name
		event.save()
		
		return HttpResponseRedirect('/reservations/reservation_lists1/')

	else:
		return render_to_response('reservations/request_form.html', context_dict, context)

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
		return render_to_response('reservations/request_details.html', context_dict, context)

@login_required
def reservation_list(request):
	context = RequestContext(request)

	requests = Requests.objects.all()

	profile = UserProfile.objects.get(user=request.user)
	context_dict = {'profile': profile, 'requests': requests}

	return render_to_response('reservations/reservation_lists.html', context_dict, context)

@login_required	
def reservation_list1(request):
	context = RequestContext(request)

	requests = Requests.objects.filter(requestedBy=request.user)

	profile = UserProfile.objects.get(user=request.user)
	context_dict = {'profile': profile, 'requests': requests}

	return render_to_response('reservations/reservation_lists1.html', context_dict, context)

