from rest_framework import serializers
from decimal import Decimal
from book.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'ISBN', 'availability_status', 'category']


# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ['id', 'name', 'description']

#     def create(self, validated_data):
#         product_id = self.context['product_id']
#         return Review.objects.create(product_id=product_id, **validated_data)