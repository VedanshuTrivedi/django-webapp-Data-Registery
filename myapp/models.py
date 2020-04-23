from django.db import models

# Create your models here.

class Item(models.Model):
    detail1 = models.TextField(max_length=20)
    detail2 = models.CharField(max_length=20)
    detail3 = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    gauge = models.CharField(max_length=10)
    quantity = models.CharField(max_length=10)
    rate = models.CharField(max_length=10)
    size = models.CharField(max_length=20)
    colour = models.CharField(max_length=20)
    podetail = models.CharField(max_length=40)
    process = models.CharField(max_length=40)
    billdetail = models.CharField(max_length=40)
    stock = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'item'
