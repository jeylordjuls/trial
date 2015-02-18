from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.forms import UserForm, UserProfileForm
from users.models import UserProfile
from reservations.models import Requests
# from reservations.views import reservation_list1, reservation_list
# Create your views here.

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
                	return HttpResponseRedirect('reservations/reservation_lists')
                else:
                    return HttpResponseRedirect('reservations/reservation_lists1')
            else:
                   
                return HttpResponse("Your account is disabled.")
        else:
                
            print "Invalid login details: {0}, {1}".format(username, password)
            # return HttpResponseRed("Invalid login details supplied.")
            return render_to_response('users/login1.html', {}, context)
    else:
        
        return render_to_response('users/login.html', {}, context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/users/login')
	
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
            'users/reg.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered, 'profile': profile,} )

@login_required
def user_list(request):
    context = RequestContext(request)

    requests = Requests.objects.all()

    profile = UserProfile.objects.get(user=request.user)
    alluser = UserProfile.objects.all()
    context_dict = {'profile': profile, 'requests': requests, 'alluser': alluser,}

    return render_to_response('users/user_lists.html', context_dict, context)