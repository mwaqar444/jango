"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest,HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.core.context_processors import csrf

from datetime import datetime
from app.models import *
def artists(request):
    artist = Artist.objects.all();
    return render_to_response('app/artists.html',{'allArtists':artist});

def artistDetails(request, id):
    artistd = Artist.objects.get(pk=id);
    return render_to_response('app/artistDetails.html',{'artist':artistd});

def artistCreate(request):
    if request.method == "GET":
        formm = artistForm();
        return render(request, 'app/create.html', {'form' : formm});
    elif request.method == "POST":
        form = artistForm(request.POST);
        form.save();
        return HttpResponseRedirect('/artists');
def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('app/login.html',c)

def auth_(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/loggedin')
    else:
        return HttpResponseRedirect('/invalid')

def loggedin(request):
    return render_to_response('app/loggedin.html',{'name':request.user.username})

def invalid(request):
    return render_to_response('app/invalid.html')
def logout(request):
    auth.logout(request)
    return render_to_response('app/logout.html')

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )
