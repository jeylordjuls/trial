from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import UserProfile
from rooms.forms import RoomForm
from reservations.views import reservation_list

# Create your views here.

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
            'rooms/room.html',
            {'room_form': room_form,'registered': registered, 'profile': profile} )