from django.contrib import admin
from .models import Unit, Melk, Ostan, City
# from django_jalali.admin.filters import JDateFieldListFilter
#from django.contrib.gis.admin import OSMGeoAdmin
import django_jalali.admin as jadmin
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin  





admin.site.register(Unit)
admin.site.register(Melk)
admin.site.register(Ostan)
admin.site.register(City)
# admin.site.register(Rosta)
# admin.site.register(Location)

# class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
#     model = Melk

# class MyInlines2(StackedInlineJalaliMixin, admin.StackedInline):
#     model = Melk

# @admin.register(Melk)
# class FirstModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
#     inlines = (MyInlines1, MyInlines2, )
#     readonly_fields = ('melk_year', 'date_field',)