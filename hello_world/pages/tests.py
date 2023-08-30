from django.test import SimpleTestCase

class HomepageTests(SimpleTestCase):
    """Testing out homepage."""
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class AboutpageTests(SimpleTestCase):
    """Testing our about page."""
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
