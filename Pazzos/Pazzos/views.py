from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    template = loader.get_template("Pazzos/index.html")
    #the second input parameter allows us to pass variables to the template (MVC view)
    context = RequestContext(request, {
        'testVariable': "Hi!"})
    return HttpResponse(template.render(context))
