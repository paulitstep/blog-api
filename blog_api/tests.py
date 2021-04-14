from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Category
from django.contrib.auth.models import User


class PostTests(APITestCase):

    def test_view_posts(self):
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_postt(self):
        self.test_category = Category.objects.create(name='django')
        self.test_user = User.objects.create_user(username='TestUser', password='testing')

        data = {"title": "new", "author": 1,
                "excerpt": "new", "content": "new"}
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
