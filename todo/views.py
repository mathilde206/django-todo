from django.shortcuts import render, redirect, get_object_or_404
from .models import Item 
from .forms import ItemForm

# Create your views here.
def get_todos(request):
    results = Item.objects.all()
    return render(request, 'todos_list.html', {'items': results})

def create_todo(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_todos)
    else:
        form = ItemForm
        
    return render(request, 'create_todo.html', {'form':form})

def edit_a_todo(request, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_todos)
    else:
        form = ItemForm(instance=item)
        return render(request, 'create_todo.html', {'form':form})


def toggle_status(request, id):
    item = get_object_or_404(Item, pk=id)
    item.done = not item.done
    item.save()
    return redirect(get_todos)