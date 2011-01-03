from django.conf.urls.defaults import *

urlpatterns = patterns('memberlist.views',
    # Uncomment the next line to enable the admin:
    (r'^$', 'index'),
    (r'^/$', 'index')
)
