from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Review(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    author = models.ForeignKey(User, related_name='review', null=False, default=1, on_delete=models.SET_DEFAULT) 
    product = models.ForeignKey(Product, related_name='reviews', null=False, default=1, on_delete=models.SET_DEFAULT) 
    
    def __str__(self):
        return self.title