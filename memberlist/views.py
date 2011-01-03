# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from meetup import MeetupUtil


def index(request):
    util = MeetupUtil()
    params = "group_id=" + util.get_group_id()
    results = util.call_remote('members', params)
    memberinfo = results['results']
    # Break the list up into columns to be painted
    retval = []
    size = len(memberinfo)
    i = 0
    slice_size = 25
    while i < size:
        chunk_end = i + slice_size
        sublist = memberinfo[i:chunk_end]
        retval.append(sublist)
        i = i + slice_size

    t = loader.get_template('members/index.html')
    c = Context({ 'member_info': retval})
    return HttpResponse(t.render(c))
