
from django.urls import path
from accounts.views import login_page , register_page , activate_email ,cart, add_to_cart , remove_cart,remove_coupon

urlpatterns = [
    path('login/', login_page , name='login'),
    path('registration/', register_page , name="register_page"),
    path('activate/<email_token>', activate_email ,name="activate_email"),
    path('cart/' , cart , name="cart"),
    path('add_to_cart/<uid>/' , add_to_cart , name = "add_to_cart"),
    path('remove_cart/<cart_item_uid>/' , remove_cart , name = "remove_cart"),
    path('remove_coupon/<cart_id>/' , remove_coupon , name= "remove_coupon"),
]