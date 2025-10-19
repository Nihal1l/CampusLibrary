from django_filters.rest_framework import FilterSet
from members.models import Member

class MemberFilter(FilterSet):
    class Meta:
        model = Member
        fields = {
            'name': ['exact']
        }