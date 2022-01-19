from books.models import Book
from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    
    def setUp(self):
        self.book1 = Book.objects.create(
            title='Władca Pierścieni',
            authors='Tolkien',
            published_date='1970',
            isbn='1231231232',
            page_count='123',
            image_link='http://books.google.com/books/content?id=DqLPAAAAMAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api',
            language='en'
        )
    
    
    def test_book_list(self):
        
        url = reverse('book_list')
        response = self.client.get(url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')
        
    def test_add_book(self):
        
        url = reverse('add_book')
        response = self.client.post(
            url, {
                'title': 'Hobbit',
                'authors': 'Tolkien'
            }, follow=True
        )
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')
        self.assertTrue(Book.objects.filter(title='Hobbit'))
        
    def test_add_book_search_import(self):
        url = reverse('add_book')
        
        response = self.client.get(
            url, {
                'q': 'Hobbit',
            }, follow=True
        )
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/add_edit.html')
        
    def test_import_book(self):
        url = reverse('import_book')
        
        response = self.client.post(
            url, {
                'title': 'Hobbit',
                'authors': 'Tolkien',
                'published_date': '1960',
                'isbn': '1231231232',
                'page_count': '123',
                'image_link': 'http://books.google.com/books/content?id=DqLPAAAAMAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api',
                'language': 'en'
                
            }, follow=True
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')
        
    def test_edit_book(self):
        book_id = Book.objects.get(title='Władca Pierścieni').id
        url = reverse('edit_book', args=[book_id])
        
        response = self.client.post(
            url, {
                'title': 'Hobbit', 'authors': 'Tolkien'
                }, follow=True
            )
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')
        self.assertEquals(Book.objects.filter(
            title='Hobbit'
        ).count(), 1)
        
    def test_soft_delete(self):
        book_id = Book.objects.get(title='Władca Pierścieni').id
        url = reverse('delete_book', args=[book_id])
        
        response = self.client.post(
            url, follow=True
            )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')
        self.assertEquals(Book.active.all().count(), 0)
        self.assertEquals(Book.objects.all().count(), 1)
