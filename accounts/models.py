from django.db import models
# Create your models here.
# Create your models here.
class Productos (models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics', null=True ,blank= True)
    desc = models.TextField(max_length=200)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
class Mochilas (models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(max_length=200)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
class Lapices (models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(max_length=200)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
class Cuadernos (models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(max_length=200)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
class Piñateria (models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(max_length=200)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
class Obsequios (models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(max_length=200)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
class Juguetes (models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(max_length=200)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)