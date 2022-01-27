from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from djet import assertions


class StudentDataTest(APITestCase, assertions.StatusCodeAssertionsMixin):

    def setUp(self) -> None:
        self.base_url = reverse('apps.student_data:student_data')
        self.signal_sent = False

    def signal_receiver(self, *args, **kwargs):
        self.signal_sent = True

    def test_anon_can_create(self):

        data = {
            "destination": "USA",
            "degree": "Undergraduate",
            "firstname": "John",
            "lastname": "Doe",
            "email": "john.doe@gmail.com",
            "phone": "0000000",
            "social_media": "john.doe",
            "major": "Engineering",
            "education": [
                {
                    "curriculum": "NCTB",
                    "level": "SSC",
                    "GPA": "5.00",
                    "Year": "2016"
                },
                {
                    "curriculum": "English Medium",
                    "level": "A Level",
                    "GPA": "4.00",
                    "Year": "2018"
                }
            ],
            "ielts": "9.0",
            "message": "How do I get a scholarship?"
        }
        response = self.client.post(self.base_url, data)

        self.assert_status_equal(response, status.HTTP_201_CREATED)
