from django.urls import path
from .views import base_views


app_name = 'naSearch'
urlpatterns = [
    path('', base_views.mainPage, name='main'),
    path('search/', base_views.index, name='index')
]
