from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Category(models.Model):
	name = models.Charfield(max_length=100)
	parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

	def __str__(self):
		return self.name 

	class Meta:
		db_table = 'category'


class Brand(models.Model):
	name = models.Charfield(max_length=100)

	def __str__(self):
		return self.name 

	class Meta:
		db_table = 'brand'
		

class Product(models.Model):
	name = models.Charfield(max_length=100)
	description = models.TextField(blank=True)
	is_digital = models.BooleanField(default=False)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	category = TreeForeignKey('Category', null=True, blank=True)

	def __str__(self):
		return self.name
	
	class Meta:
		db_table = 'product'
