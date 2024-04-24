from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BorrowBook
from .serializers import BorrowBookSerializer
import requests
from rest_framework import status
@api_view(['POST'])
def create_borrow_book(request):
    # Lấy idbook từ service khác qua URL
    book_url = 'http://127.0.0.1:5000/api/books/'  
    try:
        response = requests.get(book_url)
        response.raise_for_status()  # Nếu có lỗi, ném ra một exception
        book_data = response.json()

        # Sử dụng idbook để tạo BorrowBook
        idbook = book_data[0].get('idbook')
        if idbook:
            borrow_book_data = {
                'idbook': idbook,
                'name_cust': request.data.get('name_cust'),
                'cccd_cust': request.data.get('cccd_cust'),
                'sdt': request.data.get('sdt'),
                'address_cust': request.data.get('address_cust'),
                'quantity': request.data.get('quantity'),
                'address_lib': request.data.get('address_lib'),
                'date_borrow': request.data.get('date_borrow'),
                'date_return_expected': request.data.get('date_return_expected'),
                'status': request.data.get('status')
            }
            serializer = BorrowBookSerializer(data=borrow_book_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return Response(serializer.errors, status=400)
        else:
            return Response({'message': 'Không thể lấy idbook từ service sách'}, status=400)
    except requests.RequestException as e:
        return Response({'message': f'Lỗi khi truy cập service sách: {e}'}, status=500)
    
@api_view(['GET'])
def get_all_borrow_books(request):
    if request.method == 'GET':
        borrow_books = BorrowBook.objects.all()
        serializer = BorrowBookSerializer(borrow_books, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def borrow_book_detail(request, borrow_book_id):
    try:
        # Lấy thông tin của phiếu mượn từ cơ sở dữ liệu
        borrow_book = BorrowBook.objects.get(idborrow=borrow_book_id)
        # Serialize thông tin phiếu mượn
        serializer = BorrowBookSerializer(borrow_book)
        # Trả về dữ liệu serialized với mã status HTTP 200 OK
        return Response(serializer.data, status=status.HTTP_200_OK)
    except BorrowBook.DoesNotExist:
        # Trả về thông báo lỗi nếu phiếu mượn không tồn tại với mã status HTTP 404 Not Found
        return Response({'message': 'Phiếu mượn không tồn tại'}, status=status.HTTP_404_NOT_FOUND)