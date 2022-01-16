from django.db import models
from isbn_field import ISBNField


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    published_date = models.DateField()
    isbn = ISBNField()
    page_count = models.DecimalField(max_digits=5, decimal_places=0)
    image_link = models.URLField(max_length=500)
    language = models.CharField(max_length=2)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    objects = models.Manager() 
    active = ActiveManager()
    
    class Meta:
        ordering = ('-created_date',)
        
    def __str__(self):
        return self.title
