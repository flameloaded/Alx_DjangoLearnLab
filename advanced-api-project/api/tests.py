from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITests(APITestCase):
    def setUp(self):
        # Create test user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()

        # Create an author
        self.author = Author.objects.create(name="Author One")

        # Create some books
        self.book1 = Book.objects.create(title="Book A", publication_year=2020, author=self.author)
        self.book2 = Book.objects.create(title="Book B", publication_year=2021, author=self.author)

        # Endpoints
        self.list_url = reverse('book-list')         # /books/
        self.detail_url = reverse('book-detail', args=[self.book1.pk])  # /books/<id>/
        self.create_url = reverse('book-create')     # /books/create/
        self.update_url = reverse('book-update', args=[self.book1.pk])  # /books/update/<id>/
        self.delete_url = reverse('book-delete', args=[self.book1.pk])  # /books/delete/<id>/

    def test_list_books(self):
        """Anyone should be able to list books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_retrieve_book_detail(self):
        """Anyone should be able to retrieve a book detail."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_requires_authentication(self):
        """Unauthenticated users cannot create books."""
        data = {'title': 'Book C', 'publication_year': 2022, 'author': self.author.pk}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Now login and try again
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_requires_authentication(self):
        """Only authenticated users can update books."""
        data = {'title': 'Book A Updated', 'publication_year': 2020, 'author': self.author.pk}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Now login and try again
        self.client.login(username='testuser', password='testpass')
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Book A Updated')

    def test_delete_book_requires_authentication(self):
        """Only authenticated users can delete books."""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        """Verify filtering works using ?title=Book A."""
        url = f"{self.list_url}?title=Book A"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all("Book A" in book['title'] for book in response.data))

    def test_search_books_by_title(self):
        """Verify searching works using ?search=Book."""
        url = f"{self.list_url}?search=Book"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_order_books_by_year(self):
        """Verify ordering works using ?ordering=publication_year."""
        url = f"{self.list_url}?ordering=publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))
