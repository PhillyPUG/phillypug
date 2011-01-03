# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from meetup import MeetupUtil

def index(request):
    util = MeetupUtil()
    params = "group_id=" + util.get_group_id()
    results = util.call_remote('events',params)
    t = loader.get_template('events/index.html')
    c = Context({ 'event_info': results['results']})
    return HttpResponse(t.render(c))

