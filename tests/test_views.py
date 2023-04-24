from django.test import TestCase
from restaurant import models
from rest_framework.renderers import JSONRenderer
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        models.Menu.objects.create(title='IceCream1', price=80, inventory=100)
        models.Menu.objects.create(title='IceCream2', price=50, inventory=110)
        models.Menu.objects.create(title='IceCream3', price=20, inventory=80)

    def test_get_all(self):
        api_response = self.client.get('/restaurant/menu')
        all_items = models.Menu.objects.all()
        all_items_serialized = MenuSerializer(all_items, many=True)
        all_items_json = JSONRenderer().render(all_items_serialized.data)
        self.assertEqual(all_items_json, api_response.content)