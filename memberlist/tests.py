"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
import memberlist.views
import json
from types import *
class SimpleTest(TestCase):

  def testMemberList(self):
    client = Client()
    response = client.get("/members/")
    # assert we got something back
    """
    Find my name in the member list
    """
    j = memberlist.views._getMeetupData()
    self.assertTrue(StringType(j))
    # if the json cant be parsed, it'll blow up and the test will fai
    self.assertTrue(ListType(json.loads(j)))
    self.assertEquals(200, response.status_code)
    self.assertTrue(response.content.find("Jason Stelzer") > 0)

