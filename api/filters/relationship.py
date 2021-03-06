import django_filters

from ..models import Relationship


class RelationshipFilter(django_filters.rest_framework.FilterSet):
    
    class Meta:
        model = Relationship
        fields = {
            'id': ['exact'],
            'name':['exact', 'icontains'],
            'is_active': ['exact'],
            'created_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],             
            'created_by': ['exact'],
        }
        ordering_fields = ('id', 'name')
        

class RelationshipFullDataFilter(django_filters.rest_framework.FilterSet):
    
    class Meta:
        model = Relationship
        fields = {
            'id': ['exact'],
            'name':['exact', 'icontains'],
            'is_active': ['exact'],
            'created_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
            'created_by__username': ['exact', 'icontains'],
            'updated_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
            'updated_by__username': ['exact', 'icontains'],
        }
        ordering_fields = ('id', 'name', 'created_at', 'created_by', 'updated_at', 'updated_by')