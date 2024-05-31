from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=50, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    CATEGORIES = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor')
    )
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=100, null=True, choices=CATEGORIES)
    description = models.TextField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered','Delivered')
    )
    # customer = 
    # product = 
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,null=True,choices=STATUS)