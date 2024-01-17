import factory 
import pytest 
import json 

pytestmark = pytest.mark.django_db

class TestCategoryEndpoints:
	endpoint = '/product/category/'

	def test_category_get(self, category_factory, api_client):
		category_factory()
		response = api_client().get(self.endpoint)
		assert response.status_code == 200
		assert len(json.loads(response.content)) == 43

class TestBrandEndpoints:
	pass

class TestProductEndpoints:
	pass