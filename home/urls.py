
from django.urls import path
from home.views import index , category 


urlpatterns = [
    path('', index , name='index',),
    path('category',category, name='category',),
]