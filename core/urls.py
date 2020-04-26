from django.urls import path,include
# from .views import UnitForm,MelkForm, UserLoginForm, UserRegisterForm
from .views import *
# from django.conf import settings
#from .views import MapWidgetListView, PointFieldGoogleWidgetView, PointFieldGoogleStaticWidgetView, PointFieldGoogleStaticOverlayWidgetView
app_name = 'core'

urlpatterns = [

        path('', index_view, name='index'),
        path('uploadcsv/', upload_csv, name='upload_csv'),
        path('downloadcsv/', download_csv, name='download_csv'),
        # path('ajax/load_cities/', load_cities, name='load_cities'),
        #path('logout/', Signout, name='logout'),
        path('login/', login_view, name='login'),
        path('logout/', logout_view, name='logout'),
        path('register/', Register_view, name='register'),
        path('unit/', UnitCreateView, name='unit_create'),
        #path('<int:id>/', UnitDetailView, name='detail'),
        path('<int:id>/update/', UnitUpdateView, name='unit_update'),
        path('<int:id>/delete/', UnitDeleteView, name='unit_delete'),
        path('melk/', MelkCreateView, name='melk_insert'),
        path('update/', MelkUpdateView, name='melk_update'),
        # path('search/', MelkFilterView, name='melk_search'),
        path('upload/', Upload_view, name='upload'),
        path('<int:id>/melkdelete/', MelkDeleteView, name='melk_delete'),
        path('brand/<int:id>', all_json_models),
        
]

