from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from ARK.forms import PazzosRegistrationForm
from ARK.forms import PazzosProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# Create your views here.
from django.http import HttpResponse

@login_required
def index(request):
    return HttpResponse("Hello, world. You're at the application")

@login_required
def profile(request):
    if request.method == 'POST':
        form = PazzosProfileForm(request.POST, instance = request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/loggedin.html')
    else:
        user = request.user
        profile = user.profile
        form = PazzosProfileForm(instance = profile)
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('profile.html', args)

def login(request):
    c = {}
    c.update(csrf(request))
    c['register'] = PazzosRegistrationForm()
    return render_to_response('login.html', c)

def logout(request):
    return render_to_response('logout.html')

def loggedin(request):
    return redirect_to_view('/ARK/profile')

def invalid_login(request):
    return render_to_response('/accounts/invalid.html')

def auth_view(request):
    email = request.POST.get("email", "")
    password = request.POST.get("password", "")
    user = auth.authenticate(email = email, password = password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin.html')
    else:
        c = {}
        c.update(csrf(request))
        c['register'] = PazzosRegistrationForm()
        c['invalid'] = True
        return render_to_response('login.html', c)

def register(request):
    if request.method == 'POST':
        form = PazzosRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

def register_success(request):
    return HttpResponseRedirect('/ARK/profile')

