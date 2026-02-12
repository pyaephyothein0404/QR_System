from django.test import TestCase
from django.urls import reverse

class TripViewTests(TestCase):

    def setUp(self):
        # Create a user for testing
        self.user = self.create_user(username='testuser', password='testpassword')
        self.superuser = self.create_superuser(username='superuser', password='superpassword')

    def test_trip_page_accessible_by_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('trip:trip_detail'))
        self.assertEqual(response.status_code, 200)

    def test_trip_page_accessible_by_superuser(self):
        self.client.login(username='superuser', password='superpassword')
        response = self.client.get(reverse('trip:trip_detail'))
        self.assertEqual(response.status_code, 200)

    def test_trip_page_not_accessible_by_anonymous_user(self):
        response = self.client.get(reverse('trip:trip_detail'))
        self.assertEqual(response.status_code, 302)  # Redirects to login page

    def test_qr_code_generation(self):
        response = self.client.get(reverse('trip:generate_qr_code'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'QR Code')  # Assuming the QR code is rendered in the response

    def test_restricted_folder_access(self):
        self.client.login(username='superuser', password='superpassword')
        response = self.client.get('/restricted-folder/')
        self.assertEqual(response.status_code, 200)  # Superuser should access

        self.client.logout()
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/restricted-folder/')
        self.assertEqual(response.status_code, 403)  # Regular user should be forbidden