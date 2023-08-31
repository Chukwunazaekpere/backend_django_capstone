from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)
   date_created = models.DateTimeField(auto_now=True)

   def fullname(self):
      return f"{self.first_name} {self.last_name}"
   fullname.short_description = 'full_name'

   def __str__(self):
      return self.first_name + ' ' + self.last_name

class Category(models.Model):
   name = models.CharField(max_length=255)
   slug = models.SlugField(editable=False)
   date_created = models.DateTimeField(auto_now=True)
   created_by = models.ForeignKey(User, related_name='menu_item_category', on_delete=models.PROTECT)


   def __str__(self):
      return self.name
   class Meta:
      verbose_name = "Menu Category"
      verbose_name_plural = "Menu Categories"


class Menu(models.Model):
   category = models.ForeignKey(Category, on_delete=models.PROTECT)
   name = models.CharField(max_length=200)
   price = models.DecimalField(decimal_places=2, max_digits=12)
   description = models.CharField(max_length=200)
   created_by = models.ForeignKey(User, on_delete=models.PROTECT)
   image = models.ImageField(upload_to='menu_item_images/%Y/%m/%d/')
   date_created = models.DateTimeField(auto_now=True)

   class Meta:
      verbose_name = "Menu Item"
      verbose_name_plural = "Menu Items"

   def __str__(self):
      return self.name

   def get_menu_details(self):
      return {
         "name": self.name,
         "description": self.description,
         "image": self.image.url,
         "price": self.price,
      }

