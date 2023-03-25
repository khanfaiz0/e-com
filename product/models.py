
from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
# Create your models here.

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True , null=True , blank=True)
    category_image = models.ImageField(upload_to="categories")


    def save(self ,*args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)


    def __str__(self) -> str:
        return self.category_name


class Colorvariant(BaseModel):
    color_name = models.CharField( max_length=100)
    price= models.IntegerField(default=0)

    def __str__(self):
        return self.color_name
    

class Sizevariant(BaseModel):
    size_name = models.CharField( max_length=100)
    price= models.IntegerField(default=0)

    def __str__(self):
        return self.size_name
    
    


class Products(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True , null = True , blank= True)
    category = models.ForeignKey(Category , on_delete = models.CASCADE , related_name='products')
    price = models.IntegerField()
    product_description = models.TextField()
    color_variant = models.ManyToManyField(Colorvariant, blank=True)
    size_variant = models.ManyToManyField(Sizevariant, blank=True)

    def save(self ,*args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Products,self).save(*args, **kwargs)


    def __str__(self) -> str:
        return self.product_name

    def get_product_price_by_size(self , size):
        return self.price + Sizevariant.objects.get(size_name = size).price




class Productimage(BaseModel):
    product = models.ForeignKey(Products , on_delete = models.CASCADE , related_name='product_img')
    image = models.ImageField(upload_to="product")



class Coupon(BaseModel):
    coupon_code = models.CharField( max_length=10)
    is_expired = models.BooleanField(default=False)
    discount_price = models.IntegerField(default=100)
    minimum_amount = models.IntegerField(default=500)


