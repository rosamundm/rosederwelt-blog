import os
from django.test import TestCase
from wagtail.tests.util import WagtailPageTests
from blog.models import MyPage


class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_server_url = 'http://' + staging_server

