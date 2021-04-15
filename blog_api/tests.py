from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from blog.models import Category, Post
from django.contrib.auth.models import User


class PostTests(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(name='django')
        self.test_user1 = User.objects.create_user(username='TestUser', password='testing')
        self.test_user2 = User.objects.create_user(username='TestUser_2', password='testing')
        self.post = Post.objects.create(category_id=1, title='Post Title', excerpt='Post Excerpt', content='Post Content',
                            slug='post-title', author_id=2, status='published')

    def test_view_posts(self):
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        self.client.login(username=self.test_user1.username, password='testing')

        data = {"title": "new", "author": 1,
                "excerpt": "new", "content": "new"}

        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_update(self):
        client = APIClient()
        client.login(username=self.test_user2.username, password='testing')

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
        client.login(username=self.test_user2.username, password='testing')

        url = reverse(('blog_api:detailcreate'), kwargs={'pk': 1})

        response = client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)