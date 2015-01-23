from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.forms import UserForm, UserProfileForm,RoomForm,ReserveForm
from accounts.models import UserProfile
from home.models import Rooms,Requests
from home.views import reservation_list1, reservation_list

def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
           
        username = request.POST['username']
        password = request.POST['password']
    	
        user = authenticate(username=username, password=password)
        # profile = UserProfile.objects.get(user=user)

        if user:
               
            if user.is_active:
                login(request, user)
                profile = UserProfile.objects.get(user=user)
                if profile.userType == 'System Administrator' : 
                	return HttpResponseRedirect('/home/reservation_lists/')
                else:
                    return HttpResponseRedirect('/home/reservation_lists1/')
            else:
                   
                return HttpResponse("Your account is disabled.")
        else:
                
            print "Invalid login details: {0}, {1}".format(username, password)
            # return HttpResponseRed("Invalid login details supplied.")
            return render_to_response('accounts/login1.html', {}, context)
    else:
        
        return render_to_response('accounts/login.html', {}, context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
	
@login_required
def register(request):
    registered = False
    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

	    profile = profile_form.save(commit=False)
	    profile.user = user

	    profile.save()
            registered = True

        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'accounts/reg.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered, 'profile': profile,} )

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

                return HttpResponseRedirect('/home/reservation_lists/')
            else:
                return HttpResponseRedirect('/home/reservation_lists1/')

        else:
	    print reserve_form.errors
            # print event_form.errors, room_form.errors, schedule_form.errors
    else:
        # event_form = EventForm()
        # room_form = RoomForm()
	# schedule_form = ScheduleForm()
	reserve_form = ReserveForm()

    return render(request,
            'accounts/reserve.html',
	     {'reserve_form': reserve_form,'registered':registered, 'rooms':rooms, 'profile':profile,})

@login_required
def add_room(request):
    registered = False
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        room_form = RoomForm(data=request.POST)


        if room_form.is_valid():
            room = room_form.save()
            room.save()

	    
            registered = True
            return reservation_list(request)

        else:
            print room_form.error
    else:
        room_form = RoomForm()
        #profile_form = UserProfileForm()

    return render(request,
            'accounts/room.html',
            {'room_form': room_form,'registered': registered, 'profile': profile} )

