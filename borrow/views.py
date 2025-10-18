from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from borrow.serializers import AddBorrowItemSerializer, BorrowItemSerializer, BorrowSerializer, UpdateBorrowItemSerializer
from borrow.models import BorrowItem, BorrowRecord 
# Create your views here.


class BorrowRecordViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowSerializer

# class ReturnViewSet(ModelViewSet):
#     http_method_names = ['post']

#     def get_queryset(self):
#         return BorrowRecord.objects.all()

#     def get_serializer_class(self):
#         return BorrowSerializer

#     def perform_create(self, serializer):
#         borrow_record = self.get_object()
#         borrow_record.returned = True
#         borrow_record.save()
#         serializer.instance = borrow_record
#         return serializer.instance

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