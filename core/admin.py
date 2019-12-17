from django.contrib import admin
from .models import Unit, Melk, Ostan, City, Rosta, Location
from django_jalali.admin.filters import JDateFieldListFilter

import django_jalali.admin as jadmin



admin.site.register(Unit)
admin.site.register(Melk)
admin.site.register(Ostan)
admin.site.register(City)
admin.site.register(Rosta)
admin.site.register(Location)

