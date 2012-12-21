from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^content/$', 'content.views.index'),
    (r'^tinymce/', include('tinymce.urls')),
    # Examples:
    # url(r'^$', 'ideafarm.views.home', name='home'),
    # url(r'^ideafarm/', include('ideafarm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
