from django.test import TestCase
from .models import Item

# Create your tests here.

class TestModel(TestCase):
    def test_done_defaults_to_false(self):
        item=Item(name='Create a Test')
        item.save()
        self.assertEqual(item.name, 'Create a Test')
        self.assertFalse(item.done)

    def test_can_create_an_item(self):
        item=Item(name='Create a Test', done=True)
        item.save()
        self.assertEqual(item.name, 'Create a Test')
        self.assertTrue(item.done)
        
    def test_shows_the_right_name(self):
        item=Item(name="hello world")
        item.save()
        self.assertEqual('hello world', str(item))