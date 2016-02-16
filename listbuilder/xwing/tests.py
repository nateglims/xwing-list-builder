from django.test import TestCase


class URLTests(TestCase):
    pages = ['/', '/xwing/', '/xwing/lists/', '/xwing/ships/']

    def test_xwing(self):
        for page in self.pages:
            response = self.client.get(page)
            self.assertEqual(response.status_code, 200)