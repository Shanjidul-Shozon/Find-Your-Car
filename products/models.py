from distutils.command.upload import upload
from email.mime import image
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from numpy import product
from django.utils.text import slugify

from base.models import BaseModel

class Category (BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True ,blank= True)
    category_image = models.ImageField(upload_to="category")

    def save(self , *args , **kwargs):
        self.slug = slugify(self.category_name)
        super(Category , self).save(*args , **kwargs)

    def __str__(self) -> str:
        return self.category_name

class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True ,blank= True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name="products")
    price = models.IntegerField()
    product_description = models.TextField()

    def save(self , *args , **kwargs):
        self.slug = slugify(self.product_name)
        super(Product , self).save(*args , **kwargs)

    def __str__(self) -> str:
        return self.product_name


class ProductImange(BaseModel):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="product_images")
    image = models.ImageField(upload_to="product")
    
