from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #r = raw_string --wysiwyg
    url(r'^add/$', 'backend.views.add', name='add'),
    url(r'^delete/(\d+)$', 'backend.views.delete', name='delete'),
    url(r'^edit/(\d+)$', 'backend.views.edit', name='edit'),
    url(r'^$', 'backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

