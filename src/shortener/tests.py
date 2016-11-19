from django.test import TestCase
from .models import KirrURL

# Create your tests here.
# ./manage.py test shortener -v 2
class KirrURLTest(TestCase):

    def test_str(self):
        my_title = KirrURL(url='www.example.com')
        self.assertEquals(
            str(my_title), 'www.example.com',
        )
