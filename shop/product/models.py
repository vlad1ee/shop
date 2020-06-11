from django.db import models
from django.contrib.auth.models import User


class Guest(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.name


class Order(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id 


class Jacket(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.IntegerField()
    photo = models.ImageField(upload_to='media', blank=True, null=True)
    slug = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.title
    

class Shirt(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.IntegerField()
    photo = models.ImageField(upload_to='media', blank=True, null=True)
    slug = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.title


class Pant(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.IntegerField()
    photo = models.ImageField(upload_to='media', blank=True, null=True)
    slug = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.title


class Footwear(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.IntegerField()
    photo = models.ImageField(upload_to='media', blank=True, null=True)
    slug = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.title


class Accessory(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.IntegerField()
    photo = models.ImageField(upload_to='media', blank=True, null=True)
    slug = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return self.title
