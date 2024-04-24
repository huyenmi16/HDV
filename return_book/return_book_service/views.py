from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ReturnBook
from .serializers import ReturnBookSerializer
import requests
from datetime import datetime, timedelta

@api_view(['POST'])
def convert_to_return_book(request, borrow_book_id):
    try:
        # Lấy thông tin của phiếu mượn từ URL khác
        borrow_book_url = f'http://127.0.0.1:8000/api/borrow-books/{borrow_book_id}/'
        response = requests.get(borrow_book_url)
        borrow_book_data = response.json()

        # Kiểm tra xem yêu cầu đã thành công hay không
        if response.status_code == 200:
            # Tính toán ngày trả mong đợi (30 ngày sau ngày mượn)
            date_borrow = datetime.strptime(borrow_book_data['date_borrow'], '%Y-%m-%d')
            date_return_expected = date_borrow + timedelta(days=30)
            date_return_expected_str = date_return_expected.strftime('%Y-%m-%d')

            # Tính toán ngày trả thực tế và số tiền phạt
            date_return_actual = datetime.now()
            days_late = (date_return_actual - date_return_expected).days
            total_money = days_late * 500 if days_late > 0 else 0

            # Tạo phiếu trả từ thông tin phiếu mượn
            return_book_data = {
                'idborrow': borrow_book_data['idborrow'],
                'idbook': borrow_book_data['idbook'],
                'name_cust': borrow_book_data['name_cust'],
                'cccd_cust': borrow_book_data['cccd_cust'],
                'sdt': borrow_book_data['sdt'],
                'address_cust': borrow_book_data['address_cust'],
                'quantity': borrow_book_data['quantity'],
                'address_lib': borrow_book_data['address_lib'],
                'date_borrow': borrow_book_data['date_borrow'],
                'date_return_expected': date_return_expected_str,
                'status': 'Đã trả',
                'date_return': date_return_actual,
                'total_money': total_money
            }

            # Trả về thông tin phiếu trả
            return Response(return_book_data, status=201)
        else:
            # Xử lý trường hợp không thể lấy được thông tin phiếu mượn từ URL khác
            return Response({'message': 'Không thể lấy thông tin phiếu mượn từ URL khác'}, status=response.status_code)
    except requests.RequestException as e:
        # Xử lý lỗi khi yêu cầu HTTP không thành công
        return Response({'message': f'Lỗi khi truy cập URL khác: {e}'}, status=500)
