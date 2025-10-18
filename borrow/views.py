from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from borrow.serializers import AddBorrowItemSerializer, BorrowItemSerializer, BorrowSerializer, UpdateBorrowItemSerializer
from borrow.models import BorrowItem, BorrowRecord 
from datetime import datetime
# Create your views here.


class BorrowRecordViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):

    
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowSerializer

class ReturnViewSet(ModelViewSet):
    http_method_names = ['post', 'delete', 'get']
    serializer_class = BorrowSerializer  # Adjust based on your needs

    def get_queryset(self):
        # Filter returns for a specific borrow if borrow_pk is provided
        borrow_pk = self.kwargs.get('borrow_pk')
        if borrow_pk:
            return BorrowRecord.objects.filter(id=borrow_pk, status='returned')
        # Fallback: return all returned records
        return BorrowRecord.objects.filter(status='returned')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        borrow_pk = self.kwargs.get('borrow_pk')
        if borrow_pk:
            context['borrow_id'] = borrow_pk
        return context

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