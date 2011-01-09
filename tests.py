import unittest
from meetup import MeetupUtil


class MeetupTests(unittest.TestCase):
    """
    Simple tests for validating my meetup util works
    """
    def test_meetup(self):
        util = MeetupUtil()
        self.assertTrue(util.get_root_url())
        self.assertTrue(util.get_group_id())
        self.assertTrue(util.get_key())
    def test_group_info(self):
        util = MeetupUtil()
        # Make a remote call.
        params = "id=" + util.get_group_id()
        results = util.call_remote('groups',params)
        self.assertTrue(results)
    def test_event_info(self):
        util = MeetupUtil()
        params = "group_id=" + util.get_group_id()
        results = util.call_remote('events',params)
        self.assertTrue(results)
if "__main__" == __name__:
    unittest.main()
