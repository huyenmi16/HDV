from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_borrow_book, name='create-borrow-book'),
    path('all/', views.get_all_borrow_books, name='get-all-borrow-books'),
    path('borrow-books/<int:borrow_book_id>/',views.borrow_book_detail , name='borrow-book-detail'),
]
