from rest_framework import serializers
from decimal import Decimal
from book.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'ISBN', 'availability_status', 'category']
