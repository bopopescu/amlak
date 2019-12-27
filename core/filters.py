import django_filters

from .models import Melk

class MelkFilter(django_filters.FilterSet):
    melk_name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
		model = Melk
        

