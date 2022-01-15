from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField()
    isbn = models.DecimalField(max_digits=13, decimal_places=0)
    page_count = models.DecimalField(max_digits=5, decimal_places=0)
    image_link = models.URLField(max_length=500)
    language = models.CharField(max_length=2)
    
    def __str__(self):
        return self.title
    
    
class Author(models.Model):
    author = models.CharField(max_length=200)
    book = models.ForeignKey(Book, 
                            related_name='authors', 
                            on_delete=models.CASCADE)
    
    def __str__(self):
        return self.author