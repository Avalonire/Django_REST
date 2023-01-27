import json
from django.test import TestCase
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APISimpleTestCase, APITestCase, force_authenticate
from django.contrib.auth.models import User
from .models import Author, Book
from .views import AuthorModelViewSet, BookModelViewSet


class TestAuthorViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors')
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors', {
            'first_name': 'Alexander',
            'last_name': 'Pushkin',
            'birthday_year': 1799
        })
        view = AuthorModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors', {
            'first_name': 'Alexander',
            'last_name': 'Pushkin',
            'birthday_year': 1799
        })
        admin = User.objects.create_superuser('admin1', 'admin@admin.com', 'admin1')
        force_authenticate(request, admin)
        view = AuthorModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        author = Author.objects.create(first_name='Alexander', last_name='Pushkin', birthday_year=1799)
        client = APIClient()
        response = client.get(f'/api/authors/{author.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        author = Author.objects.create(first_name='Alexander', last_name='Pushkin', birthday_year=1799)
        client = APIClient()
        response = client.put(f'/api/authors/{author.id}', {
            'first_name': 'Asdfg',
            'last_name': 'Glkof',
            'birthday_year': '1923'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        author = Author.objects.create(first_name='Alexander', last_name='Pushkin', birthday_year=1799)
        client = APIClient()
        admin = User.objects.create_superuser('admin1', 'admin@admin.com', 'admin1')
        client.login(username='admin1', password='admin1')
        response = client.put(f'/api/authors/{author.id}', {
            'first_name': 'Asdfg',
            'last_name': 'Glkof',
            'birthday_year': '1923'
        })
        author = Author.objects.get(pk=author.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.first_name, 'Asdfg')
        self.assertEqual(response.last_name, 'Glkof')
        self.assertEqual(response.birthday_year, '1923')
        client.logout()


class TestMatch(APISimpleTestCase):
    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)


class TestBookViewSet(APITestCase):
    def test_get_lists(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, response.HTTP_200_OK)

    def test_edit_book_admin(self):
        # author = Author.objects.create(first_name='Alexander', last_name='Pushkin', birthday_year=1799)
        # book = Book.objects.create(name='Ruslan and Ludmila', author=author)
        # book.author.add(author)
        # book.save()

        book = mixer.blend(Book)

        admin = User.objects.create_superuser('admin1', 'admin@admin.com', 'admin1')
        self.client.login(username='admin1', password='admin1')
        response = self.client.put(f'/api/books/{book.id}/', {'name': 'Ace', 'author': book.author.name})

        book = Book.objects.get(pk=book.id)
        self.assertEqual(response.status_code, response.HTTP_200_OK)
        self.assertEqual(book.name, 'Ace')
        self.client.logout()
