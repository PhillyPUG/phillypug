from django.conf.urls.defaults import *

urlpatterns = patterns('events.views',
    # Uncomment the next line to enable the admin:
    (r'^$', 'index'),
    (r'^/$', 'index')
)
