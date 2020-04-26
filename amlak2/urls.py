
# from django.conf.urls.defaults import *
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url




urlpatterns = [
    path('admin/', admin.site.urls),
   # path('api-auth/', include('rest_framework.urls')),
    path('core/', include('core.urls',namespace='core')),
    path('report_builder/', include('report_builder.urls')),
]

# urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)