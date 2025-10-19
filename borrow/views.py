from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from borrow.serializers import AddBorrowItemSerializer, BorrowItemSerializer, BorrowSerializer, UpdateBorrowItemSerializer, UpdateBorrowSerializer
from borrow.models import BorrowItem, BorrowRecord 
from datetime import datetime
# Create your views here.


class BorrowRecordViewSet(ModelViewSet):

    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_class = BorrowSerializer

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return UpdateBorrowSerializer
        
        return BorrowSerializer

    def get_queryset(self):
        return BorrowRecord.objects.all()

    def perform_create(self, serializer):
        serializer.save(borrowed_at=datetime.now())

class ReturnViewSet(ModelViewSet):
    http_method_names = ['delete', 'get']  # Add 'post' if you want to create returns
    serializer_class = BorrowSerializer  # Required by DRF
    def get_queryset(self):
        return BorrowRecord.objects.filter(
            status__iexact='returned'
        )
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Mark all associated books as available
        borrow_items = BorrowItem.objects.filter(borrow=instance)
        for item in borrow_items:
            book = item.book
            book.availability_status = True
            book.save()
        return super().destroy(request, *args, **kwargs)

class BorrowItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddBorrowItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateBorrowItemSerializer
        return BorrowItemSerializer

    def get_serializer_context(self):
        return {'borrow_id': self.kwargs['borrow_pk']}

    def get_queryset(self):
        return BorrowItem.objects.filter(borrow_id=self.kwargs['borrow_pk'])