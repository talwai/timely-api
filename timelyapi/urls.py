from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'webapp.views.home', name='home'),
     url(r'^loggedin/$', 'webapp.views.loggedin', name='loggedin'),
     #url(r'^timelyapi/', include('timelyapi.foo.urls')),
     url(r'', include('social_auth.urls')),

     # current API url
     url(r'api/v1/locations', 'webapp.views.locations', name='locations'),
     

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
