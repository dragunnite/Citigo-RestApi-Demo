from django.db import models

class Product(models.Model):
	idProduct = models.IntegerField(default = 0)
	title = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	rating = models.FloatField()
	quantity = models.IntegerField()
	price = models.FloatField()
	thumburl = models.CharField(max_length=200)
	infourl = models.CharField(max_length=200)