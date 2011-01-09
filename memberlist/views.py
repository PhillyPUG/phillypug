# Create your views here.
import json
from django.template import Context, loader
from django.http import HttpResponse
from meetup import MeetupUtil

'''
Get the Member Info for the philly pug and marshal it into a json object
that the info page can use to render.
'''
def index(request):
  # Break the list up into columns to be painted
  t = loader.get_template('members/index.html')
  info = _getMeetupData()
  c = Context({ 'member_info': "%s" % info})
  return HttpResponse(t.render(c))

def _getMeetupData():
  '''
  Returns a stringified json object suitable for the browser to load and use.
  '''
  util = MeetupUtil()
  params = "group_id=" + util.get_group_id()
  wrapper = util.call_remote('members', params)
  results = wrapper['results']
  return json.dumps(results)