from django.db import models

# Create your models here.

class Amenities(models.Model):
	class Meta:
		verbose_name_plural ="Amenities"

	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name



class Hotels(models.Model):
	class Meta:
		verbose_name_plural ="Hotels"

	hotel_name = models.CharField(max_length=100)
	hotel_description = models.TextField()
	hotel_image = models.CharField(max_length=500)
	price = models.IntegerField()
	Amenities = models.ManyToManyField(Amenities)

	def __str__(self):
		return self.hotel_name

	

