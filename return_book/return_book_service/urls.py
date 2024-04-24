# urls.py trong return_book_service
from django.urls import path
from . import views

urlpatterns = [
    path('convert-to-return/<int:borrow_book_id>/', views.convert_to_return_book, name='convert-to-return-book'),
]
