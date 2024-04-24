from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def get_book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def update_book_quantity(request, book_id):
    if request.method == 'POST':
        data = request.POST
        quantity = data.get('quantity')

        # Lấy đối tượng sách từ cơ sở dữ liệu hoặc trả về lỗi nếu không tồn tại
        book = get_object_or_404(Book, idbook=book_id)

        # Cập nhật số lượng sách
        book.quantity += int(quantity)
        book.save()

        return JsonResponse({'success': True, 'message': 'Cập nhật số lượng sách thành công'})

    return JsonResponse({'success': False, 'message': 'Yêu cầu không hợp lệ'}, status=400)