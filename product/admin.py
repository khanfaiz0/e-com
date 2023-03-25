from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Coupon)

class ProductimageAdmin(admin.StackedInline):
    model = Productimage

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product_name','price' ]
    inlines = [ProductimageAdmin]

@admin.register(Colorvariant)
class ColorvariantAdmin(admin.ModelAdmin):
    list_display = ['color_name','price' ]
    model = Colorvariant

@admin.register(Sizevariant)
class SizevariantAdmin(admin.ModelAdmin):
    list_display = ['size_name','price' ]
    model = Sizevariant


admin.site.register(Products, ProductsAdmin)

admin.site.register(Productimage)

# Register your models here.
