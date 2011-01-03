# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from meetup import MeetupUtil

def index(request):
    util = MeetupUtil()
    params = "id=" + util.get_group_id()
    results = util.call_remote('groups',params)
    info = results['results']
    info = info[0]
    info = info['description']
    t = loader.get_template('about/index.html')
    c = Context({ 'info': info})
    return HttpResponse(t.render(c))
