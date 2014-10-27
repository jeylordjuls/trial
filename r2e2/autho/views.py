from django.shortcuts import render
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    csrfContext = RequestContext(request)
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return render_to_response('untitled.html',{'state':state, 'username': username}, csrfContext)
            else:
                state = "Your account is not active, please contact the site admin."
                return render_to_response('auth.html',{'state':state, 'username': username}, csrfContext)
        else:
            state = "Your username and/or password were incorrect."
            return render_to_response('auth.html',{'state':state, 'username': username}, csrfContext)
    return render_to_response('auth.html',{'state':state, 'username': username}, csrfContext)

def logout_view(request):
    logout(request)
    csrfContext = RequestContext(request)
    return render_to_response('out.html', csrfContext)

# Create your views here.
