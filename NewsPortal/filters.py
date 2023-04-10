from django.forms import DateInput
from django_filters import FilterSet, DateFilter

from .models import Post



class PostFilter(FilterSet):
    date = DateFilter(field_name='post_time', widget=DateInput(attrs={'type': 'date'}), label='Не ранее чем',
                      lookup_expr='date__gte')

    class Meta:
        model = Post

        fields = {

            'post_title': ['icontains'],

            'post_author__user': ['exact'],

        }
