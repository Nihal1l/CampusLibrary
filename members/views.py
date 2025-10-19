from rest_framework.response import Response
from rest_framework import status
from .serializers import MemberSerializer
from members.models import Member
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from members.filters import MemberFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from book.paginations import DefaultPagination

class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MemberFilter
    pagination_class = DefaultPagination
    search_fields = ['name', 'email']
    ordering_fields = ['created_at']