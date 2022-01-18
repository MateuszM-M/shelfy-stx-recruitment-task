from django.urls import path

from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add-book', views.add_book, name='add_book'),
    path('import-book/', views.import_book, name='import_book'),
    path('edit-book/<int:pk>', views.edit_book, name='edit_book'),
    path('delete-book/<int:pk>', views.delete_book, name='delete_book'),
]