from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'mongoadmin/login.html'}),
    url(r'^accounts/logout/', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='auth_logout'),

    # Examples:
    # url(r'^$', 'mongoadmin_project.views.home', name='home'),
     url(r'^', include('mongoadmin_project.mongoadmin.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
