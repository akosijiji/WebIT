from .models import Client
from django.db.models import Case, When
import django_filters


class ClientFilter(django_filters.FilterSet):

    client_name = django_filters.CharFilter(lookup_expr='icontains')
    phone_number = django_filters.NumberFilter(lookup_expr='icontains')
    email_address = django_filters.CharFilter(lookup_expr='icontains')
    suburb = django_filters.CharFilter(lookup_expr='icontains')

    CHOICES = (
        (1, 'Client Name'),
        (2, 'Phone Number'),
        (3, 'Email Address'),
        (4, 'Suburb'),
    )

    ordering = django_filters.ChoiceFilter(
        label='Sort by', choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Client
        fields = ['client_name', 'phone_number', 'email_address', 'suburb']

    def filter_by_order(self, queryset, name, value):
        if value == '1':
            expression = 'client_name'
        elif value == '2':
            expression = 'phone_number'
        elif value == '3':
            expression = 'email_address'
        else:
            expression = 'suburb'
        return queryset.order_by(expression)
