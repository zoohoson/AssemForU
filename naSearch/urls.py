from django.urls import path
from .views import base_views


app_name = 'naSearch'
urlpatterns = [
    # base_views.py
    path('', 
        base_views.index, name='index'),
    path('<int:bill_id>/', base_views.detail, name='detail'),
]