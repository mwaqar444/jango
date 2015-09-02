"""
Definition of urls for Practice_DataBaseFun.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^artists$','app.views.artists',name='artists'),
    url(r'^artists/(?P<id>\d+)$','app.views.artistDetails',name='artistDetails'),
    url(r'^create$','app.views.artistCreate',name='artistCreate'),
    url(r'^login$','app.views.login',name='login'),
    url(r'^auth$','app.views.auth_',name='auth_'),
    url(r'^logout$','app.views.logout',name='logout'),
    url(r'^loggedin$','app.views.loggedin',name='loggedin'),
    url(r'^invalid$','app.views.invalid',name='invalid'),

    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
