from django.shortcuts import get_object_or_404
from django.test import TestCase
from .forms import Item
from .models import Item

# Create your tests here.
class TestTodoViews(TestCase):
    def test_get_home_page(self):
        page=self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'todos_list.html')
        
    def test_get_add_todo(self):
        page=self.client.get("/add/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'create_todo.html')
    
    def test_get_edit_todo(self):
        item = Item(name= 'test')
        item.save()
        
        page=self.client.get("/edit/{0}".format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'create_todo.html')
        
    def test_get_404_for_wrong_id(self):
        page=self.client.get('/edit/99')
        self.assertEqual(page.status_code, 404)
        
    def test_create_new_todo(self):
        response = self.client.post('/add/', {'name': 'Create a test'})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False )
        
    def test_edit_a_todo(self):
        item = Item(name='hello world')
        item.save()
        id = item.id
        
        response = self.client.post("/edit/{0}".format(id), {"name": "A different name"})
        
        item=get_object_or_404(Item, pk=id)
        
        self.assertEqual(item.name,'A different name')
        
    def test_toggle_status(self):
        item = Item(name='test')
        item.save()
        reponse = self.client.post('/toggle/{0}'.format(item.id))
        item = get_object_or_404(Item, pk=item.id)
        self.assertTrue(item.done)