from django.core import mail
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Notification

# Create your tests here.


class NotificationTests(APITestCase):
    def test_send_email(self):
        data = {
            "email": "test@example.com",
            "subject": "Test Email",
            "message": "This is a test.",
        }
        response = self.client.post("/api/send-notification/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Test Email")
