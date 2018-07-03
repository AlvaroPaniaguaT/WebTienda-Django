from django.db import models

# Create your models here.

class Product(models.Model):
    p_type = models.CharField(max_length=200, default='')
    price = models.FloatField()
    stock = models.IntegerField()
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default='')
    external_url = models.CharField(max_length=200, default='')
    def is_available(self):
        return self.stock > 0

class Bikes(Product):
    brand = models.CharField(max_length=200)
    b_type = models.CharField(max_length=200)

class CD(Product):
    author = models.CharField(max_length=200)
    cd_genre = models.CharField(max_length=200)

class Books(Product):
    author = models.CharField(max_length=200)
    book_genre = models.CharField(max_length=200)

class BuyOrders(models.Model):
    date = models.DateField()
    product_n = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()
    payMeth = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    add_comments = models.CharField(max_length=200)
    confirmed = models.BooleanField()
