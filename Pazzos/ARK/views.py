from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
#from ARK.forms import PazzosRegistrationForm
#from ARK.forms import PazzosProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
import pdb
from ARK.admin import PazzosCreationForm

# Create your views here.
from django.http import HttpResponse

@login_required
def index(request):
    return HttpResponse("Hello, world. You're at the application")

@login_required
def profile(request):
    #if request.method == 'POST':
    #    form = PazzosProfileForm(request.POST, instance = request.user.profile)
    #    if form.is_valid():
    #        form.save()
    #        return HttpResponseRedirect('/accounts/loggedin.html')
    #else:
    #    user = request.user
    #    profile = user.profile
    #    form = PazzosProfileForm(instance = profile)
    args = {}
    args.update(csrf(request))
    
    #args['form'] = form
    
    return render_to_response('profile.html', args)

def login(request):
    c = {}
    c.update(csrf(request))
    c['register'] = PazzosCreationForm()
    return render_to_response('login.html', c)

def logout(request):
    return render_to_response('logout.html')

def loggedin(request):
    return redirect_to_view('/ARK/profile')

def auth_view(request):
    #not sure why, but the username string is required in order to properly extract the
    #email address that's being passed in
    email = request.POST.get("username", "")
    password = request.POST.get("password", "")
    #pdb.set_trace()
    user = auth.authenticate(username = email, password = password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin.html')
    else:
        c = {}
        c.update(csrf(request))
        c['register'] = PazzosCreationForm()
        c['invalid'] = True
        return render_to_response('login.html', c)

def register(request):
    if request.method == 'POST':
        form = PazzosCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

def register_success(request):
    return HttpResponseRedirect('/ARK/profile')

