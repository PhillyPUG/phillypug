import ConfigParser
from urllib import URLopener
import json
from django.http import HttpResponse
from django.conf import settings


class MeetupUtil:
    """
    Convenience wrapper for calling the meetup.com API.
    """

    def __init__(self):
        parser = ConfigParser.ConfigParser()
        parser.read(settings.MEETUP_CFG)
        self.root_url = parser.get('meetup','url_base')
        self.key = parser.get('meetup','key')
        self.group_id = parser.get('meetup','group_id')

    def get_root_url(self):
        return self.root_url
    def get_group_id(self):
        return self.group_id
    def get_key(self):
        return self.key
    def call_remote(self,category,params):
        '''
        The meetup api is set up such that the root url does not
        change much other than the'name' of the thing you call into.

        In other words, I can just use category to sprintf my way to a
        valid url, then tack on the rest of the query string specified
        in params.
        '''
        url = self.root_url
        url = url % (category)
        # Every call has to include key
        url = url + "?" + params + "&key=" + self.key
        client = URLopener()
        request = client.open(url)
        raw_str = request.read()
        results = json.loads(raw_str)
        # Let the caller interpret the results of the call. Both the
        # meta info and the results are passed back
        return results
        
