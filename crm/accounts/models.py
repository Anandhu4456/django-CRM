from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=30, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self) -> str:
        return self.name
    
    
        