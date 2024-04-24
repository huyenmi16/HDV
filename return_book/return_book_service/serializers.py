# serializers.py trong return_book_service
from rest_framework import serializers
from .models import ReturnBook

class ReturnBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnBook
        fields = '__all__'