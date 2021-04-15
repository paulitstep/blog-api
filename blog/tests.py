from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


class Test_Create_Post(TestCase):

    def setUp(self):
        Category.objects.create(name='django')
        User.objects.create_user(username='TestUser', password='testing')
        Post.objects.create(category_id=1, title='Post Title', excerpt='Post Excerpt', content='Post Content',
                            slug='post-title', author_id=1, status='published')

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        category = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'TestUser')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(excerpt, 'Post Excerpt')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), "Post Title")
        self.assertEqual(str(category), "django")

