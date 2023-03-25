from django.contrib import admin
from django.urls import path
from product.views import *

urlpatterns = [
    path('<slug>/', get_product , name= "get_products"),
    path('<category_name>/', get_categories , name = "get_categories"),
    
]