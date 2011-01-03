from django.conf.urls.defaults import *

urlpatterns = patterns('about.views',
    # Uncomment the next line to enable the admin:
    (r'^$', 'index'),
    (r'^/$', 'index')
)
