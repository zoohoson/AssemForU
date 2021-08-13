from django.urls import path
from .views import base_views


app_name = 'naSearch'
urlpatterns = [
    path('', base_views.main_page, name='main'),
    path('index/', base_views.index, name='index'),
    path('index/<int:bill_no>/', base_views.detail, name='detail'),
]
