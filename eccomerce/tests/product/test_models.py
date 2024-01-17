import pytest
from django.test import TestCase

class TestCategoryModel:
	def test_str_method(self, category_factory):
		# Arrange
		# Act
		x = category_factory()

		# Assert
		assert x.__str__() == "test_category"

class TestBrandModel:
	def test_str_method(self, brand_factory):
	x = brand_factory

	assert x.__str__() == "test_brand"

class TestProductModel:
	def test_str_method(self, product_factory):
		obj = product_factory(name="test_product")
		assert obj.__str__() == "test_product"


		