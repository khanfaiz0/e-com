#from distutils.command.upload import upload
#from email.policy import default
#from unittest.util import _MAX_LENGTH
import uuid

from base.email import send_account_activation_email
from base.models import BaseModel
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from product.models import Coupon, Products ,Colorvariant,Sizevariant

# Create your models here.

class Profile(BaseModel):
    user = models.OneToOneField(User , on_delete = models.CASCADE , related_name='profile')
    is_email_varified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100,null=True , blank=True)
    profile_image = models.ImageField(upload_to='profile')

    def get_cart_count(self):
        return CartItems.objects.filter(cart__is_paid = False , cart__user = self.user).count()

class Cart(BaseModel):
    user= models.ForeignKey(User,on_delete=models.CASCADE , related_name = 'carts')
    coupon = models.ForeignKey(Coupon , on_delete=models.SET_NULL , null=True, blank=True)
    is_paid = models.BooleanField(default = False)

    def get_cart_total(self):
        cart_item = self.cart_item.all()
        price =[]
        for cart_item in cart_items:
            price.append(cart_item.product.price)
            if cart_item.color_variant:
                color_variant_price = cart_item.color_variant.price
                price.append(color_variant.price)
            if cart_item.size_variant:
                size_variant_price = cart_item.size_variant.price
                price.append(size_variant_price)

            if self.coupon:
                return sum(price) - self.coupon.discount_price

        return sum(price)


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE , related_name="cart_item")
    product = models.ForeignKey(Products , on_delete=models.SET_NULL , null = True,  blank = True)
    color_variant = models.ForeignKey(Colorvariant , on_delete=models.SET_NULL , null= True , blank = True)
    size_variant =models.ForeignKey(Sizevariant, on_delete=models.SET_NULL , null = True , blank = True)

    def get_product_price(self):
        price = [self.product.price]

        if self.color_variant:
            color_variant_price = self.color_variant.price
            price.append(color_variant_price)
        if self.size_variant:
            size_variant_price = self.size_variant.price
            price.append(size_variant_price)
        return sum(price)



# creation of signal for email 

@receiver(post_save , sender= User)
def send_email_token(sender , instance , created ,**kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(user = instance , email_token = email_token)
            email= instance.email
            send_account_activation_email(email , email_token)

    except Exception as e:
        print(e)
