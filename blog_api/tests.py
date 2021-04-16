from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from blog.models import Category, Post


class PostTests(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(name='django')
        db = get_user_model()
        self.test_user1 = db.objects.create_user(email='testuser1@gmail.com', user_name='TestUser', password='testing')
        self.test_user2 = db.objects.create_user(email='testuser2@gmail.com', user_name='TestUser_2', password='testing')
        self.post = Post.objects.create(category_id=1, title='Post Title', excerpt='Post Excerpt', content='Post Content',
                            slug='post-title', author_id=2, status='published')

    def test_view_posts(self):
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        client = APIClient()
        url_login = reverse('token_obtain_pair')
        resp = self.client.post(url_login, {"email": self.test_user1.email, "password": "testing"}, format='json')
        token = resp.data.get('access')
        client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

        data = {"title": "new", "author": 1,
                "excerpt": "new", "content": "new"}

        url = reverse('blog_api:listcreate')
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_update(self):
        client = APIClient()
        url_login = reverse('token_obtain_pair')
        resp = self.client.post(url_login, {"email": self.test_user2.email, "password": "testing"}, format='json')
        token = resp.data.get('access')
        client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

        url = reverse(('blog_api:detailcreate'), kwargs={'pk': 1})

        response = client.put(url, {
            'title': 'Updated',
            'author': 2,
            'excerpt': 'Updated',
            'content': 'Updated',
            'status': 'published'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_delete(self):
        client = APIClient()
        url_login = reverse('token_obtain_pair')
        resp = self.client.post(url_login, {"email": self.test_user2.email, "password": "testing"}, format='json')
        token = resp.data.get('access')
        client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

        url = reverse(('blog_api:detailcreate'), kwargs={'pk': 1})

        response = client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)