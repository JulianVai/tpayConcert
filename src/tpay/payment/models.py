from django.db import models

# Create your models here.

class EventFeatures(models.Model):
    id_event = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    quantity_total = models.IntegerField(default=0)
    price_unit = models.IntegerField(default=0)
    

class OrderTickets(models.Model):
    order_id = models.CharField(max_length=64)
    quantity_sold = models.IntegerField(default=0)
    state = models.IntegerField()
    price_total = models.IntegerField(default=0)
    date_create = models.DateField()
    exp_date = models.DateField()
    order_description = models.CharField(max_length=64)

class User(models.Model):
    nombre = models.CharField(max_length = 64)
    apellido = models.CharField(max_length= 64)
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    is_host = models.BooleanField(default=False)


