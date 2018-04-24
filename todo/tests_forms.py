from django.test import TestCase
from .forms import ItemForm

# Create your tests here.
class TestTodoForm(TestCase):
    def test_can_create_an_item_with_just_a_name(self):
        form = ItemForm({'name':'test'})
        self.assertTrue(form.is_valid())

    def test_correct_message_for_empty_name(self):
        form=ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'],[u'This field is required.'] )