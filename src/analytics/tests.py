from django.test import TestCase
from .models import ClickEvent
# Create your tests here.
# ./manage.py test shortener -v 2

class ClickEventTest(TestCase):

    def test_str(self):
        my_title = ClickEvent(url='www.example.com')
        self.assertEquals(
            str(my_title), 'www.example.com'
        )
