from django.test import TestCase
from django.urls import reverse

from .models import Teacher


class DeleteTeacherTests(TestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create(
            name='Test Teacher',
            subject='Math',
            email='teacher@example.com',
            contact_number='1234567890',
        )
        self.delete_url = reverse('delete_teacher', args=[self.teacher.pk])

    def test_delete_requires_post(self):
        response = self.client.get(self.delete_url)

        self.assertEqual(response.status_code, 405)
        self.assertTrue(Teacher.objects.filter(pk=self.teacher.pk).exists())

    def test_post_deletes_teacher(self):
        response = self.client.post(self.delete_url)

        self.assertRedirects(response, reverse('teachers_list'))
        self.assertFalse(Teacher.objects.filter(pk=self.teacher.pk).exists())
