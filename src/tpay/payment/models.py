from djongo import models

# Create your models here.

class ConcertTickets(models.Model):
    id_event = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    quantity_total = models.IntegerField(default=0)
    price_unit = models.IntegerField(default=0)
    
    def __str__(self):
        return "Concert " + self.description + " with " + self.quantity_total + "tickets at " + str(self.price_unit)

class OrderTickets(models.Model):
    order_id = models.CharField(max_length=64)
    quantity_sold = models.IntegerField(default=0)
    state = models.IntegerField()
    price_total = models.IntegerField(default=0)
    date_create = models.DateField()
    exp_date = models.DateField()
    order_description = models.CharField(max_length=64)
