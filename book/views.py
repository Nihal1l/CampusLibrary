from rest_framework.response import Response
from rest_framework import status
from book.models import Book
from book.serializers import BookSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from book.paginations import DefaultPagination

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    pagination_class = DefaultPagination
    search_fields = ['title', 'author__name']
    ordering_fields = ['created_at']

    # def destroy(self, request, *args, **kwargs):
    #     book = self.get_object()
    #     if book.stock > 10:
    #         return Response({'message': "Book with stock more than 10 could not be deleted"})
    #     self.perform_destroy(book)
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# class ReviewViewSet(ModelViewSet):
#     serializer_class = ReviewSerializer

#     def get_queryset(self):
#         return Review.objects.filter(product_id=self.kwargs['product_pk'])

#     def get_serializer_context(self):
#         return {'product_id': self.kwargs['product_pk']}