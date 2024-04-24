from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_book_list, name='book-list'),
    path('books/update/<int:book_id>', views.update_book_quantity, name='update-book-quantity'),
]
