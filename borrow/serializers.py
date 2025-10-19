from typing import __all__
from book.models import Book
from rest_framework import serializers
from borrow.models import BorrowRecord , BorrowItem


class SimpleBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'availability_status']


class AddBorrowItemSerializer(serializers.ModelSerializer):
    book_id = serializers.IntegerField()

    class Meta:
        model = BorrowItem
        fields = ['id', 'book_id', 'quantity']

    def save(self, **kwargs):
        borrow_id = self.context['borrow_id']
        book_id = self.validated_data['book_id']
        quantity = self.validated_data['quantity']

        # Get the book and check availability
        book = Book.objects.get(pk=book_id)
        
        if not book.availability_status:
            raise serializers.ValidationError("Book is not available for borrowing")
        else:
            book.availability_status = False  # Mark book as not available
            book.save()
            try:
                borrow_item = BorrowItem.objects.get(
                    borrow_id=borrow_id, book_id=book_id)
                borrow_item.quantity += quantity
                borrow_item.save()
                self.instance = borrow_item
            except BorrowItem.DoesNotExist:
                self.instance = BorrowItem.objects.create(
                    borrow_id=borrow_id, **self.validated_data)

        return self.instance

    def validate_book_id(self, value):
        if not Book.objects.filter(pk=value).exists():
            raise serializers.ValidationError(
                f"Book with id {value} does not exist")
        return value
class UpdateBorrowItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BorrowItem
        fields = ['quantity']

class UpdateBorrowSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BorrowRecord
        fields = ['status']

class BorrowItemSerializer(serializers.ModelSerializer):
    book = SimpleBookSerializer()

    class Meta:
        model = BorrowItem
        fields = ['id', 'book', 'quantity']


class BorrowSerializer(serializers.ModelSerializer):
    items = BorrowItemSerializer(many=True, read_only=True)

    class Meta:
        model = BorrowRecord
        fields = ['id', 'member', 'borrow_date', 'return_date', 'status', 'items']

        
