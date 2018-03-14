from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    quantity = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0)
    typeOf = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='item/%Y/%m/%d/', default='item/default_item.jpg')

    def __str__(self):
        return self.name

class Review(models.Model):
    title = models.CharField(max_length=250)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title