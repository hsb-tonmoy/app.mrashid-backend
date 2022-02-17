from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from djet import assertions

from apps.student_data.models import StudentData

User = get_user_model()

data = {
    "destination": "USA",
    "degree": "Undergraduate",
    "first_name": "John",
    "last_name": "Doe",
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
    "english_proficiency": "toefl",
    "english_proficiency_score": "112",
    "message": "How do I get a scholarship?"
}


class StudentDataTest(APITestCase, assertions.StatusCodeAssertionsMixin):

    def setUp(self) -> None:
        self.base_url = reverse('student_data:student_data-list')
        self.signal_sent = False

    def signal_receiver(self, *args, **kwargs):
        self.signal_sent = True

    def test_anon_can_create(self):

        response = self.client.post(self.base_url, data, format='json')

        self.assert_status_equal(response, status.HTTP_201_CREATED)

    def test_anon_cannot_get_or_retrieve(self):

        response = self.client.get(self.base_url)

        self.assert_status_equal(response, status.HTTP_401_UNAUTHORIZED)


class StudentDataOwnerCanRetrieve(APITestCase, assertions.StatusCodeAssertionsMixin):

    def setUp(self) -> None:

        self.base_url = reverse('student_data:student_data-list')

        self.user_email = 'johndoe@gmail.com'
        self.user_password = 'top_secret'

        self.user = User.objects.create_user(
            first_name='john', last_name='doe', email=self.user_email, password=self.user_password)

        student_data = self.client.post(
            self.base_url, data, format='json')

        self.student_data_id = student_data.data['id']

        self.student = StudentData.objects.get(id=self.student_data_id)

        self.signal_sent = False

    def signal_receiver(self, *args, **kwargs):
        self.signal_sent = True

    def test_owner_can_retrieve(self):

        if self.user:
            self.user.student = self.student
            self.user.save()
        self.student_data_url = reverse(
            'student_data:student_data-detail', kwargs={'pk': self.student_data_id})

        self.client.login(email=self.user_email, password=self.user_password)

        response = self.client.get(self.student_data_url)

        self.assert_status_equal(response, status.HTTP_200_OK)
