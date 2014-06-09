from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
#from ARK.forms import PazzosRegistrationForm
#from ARK.forms import PazzosProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
import pdb
from ARK.admin import PazzosCreationForm, PazzosChangeForm
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse

@login_required
def index(request):
    return render_to_response('ARK/index.html')

@login_required
def profile(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        #pdb.set_trace()
        form = PazzosChangeForm(request.POST, instance = request.user)
        #password = form.fields['password']
        
        if form.is_valid():
            form.save()
            args['form'] = form
    else:
        form = PazzosChangeForm(instance = request.user)
        args['form'] = form
    return render_to_response('ARK/profile.html',args)


#@login_required
#def profile(request):
#    if request.method == 'POST':
#        form = PazzosProfileForm(request.POST, instance = request.user.profile)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect('/accounts/loggedin.html')
#    else:
#        user = request.user
#       # profile = user.profile
#        #form = PazzosProfileForm(instance = profile)
#    args = {}
#    args.update(csrf(request))
#    
#    #args['form'] = form
#    
#    return render_to_response('profile.html', args)

def login(request):
    c = {}
    testVar = request.GET.get('next')
    if testVar:
        c['next'] = testVar
    c.update(csrf(request))
    c['register'] = PazzosCreationForm()
    return render_to_response('ARK/login.html', c)

def logout(request):
    auth.logout(request)
    return render_to_response('ARK/logout.html')

def loggedin(request):
    return redirect_to_view('ARK/profile')

def auth_view(request):
    email = request.POST.get("email", "")
    password = request.POST.get("password", "")
    #pdb.set_trace()
    user = auth.authenticate(username = email, password = password)
    if user is not None:
        auth.login(request, user)
        nextVar = request.POST.get("next","")
        if nextVar != "":
            return HttpResponseRedirect(nextVar)
        return redirect('ARK.views.index')
    else:
        c = {}
        c.update(csrf(request))
        c['register'] = PazzosCreationForm()
        c['invalid'] = True
        return render_to_response('ARK/login.html', c)

def register(request):
    if request.method == 'POST':
        form = PazzosCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #pdb.set_trace()
            user = auth.authenticate(email = form.data['email'], password = form.data['password1'])
            #THIS CHECK SHOULD NEVER FAIL IF WE'RE LOGGING IN SOMEONE WHO JUST REGISTERED
            if user is not None:
                auth.login(request, user)
                nextVar = request.POST.get("next", "")
                if nextVar != "":
                    return HttpResponseRedirect(nextVar)
                return redirect ('ARK.views.profile')

def register_success(request):
    return HttpResponseRedirect('ARK/profile')

