from django.shortcuts import render, get_object_or_404, redirect
from .models import CrochetItem
from .forms import CrochetItemForm

def index(request):
    items = CrochetItem.objects.all()
    return render(request, 'crochet_store/index.html', {'items': items})

def create_item(request):
    if request.method == 'POST':
        form = CrochetItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CrochetItemForm()
    return render(request, 'crochet_store/form.html', {'form': form})

def edit_item(request, id):
    item = get_object_or_404(CrochetItem, id=id)
    if request.method == 'POST':
        form = CrochetItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CrochetItemForm(instance=item)
    return render(request, 'crochet_store/form.html', {'form': form})

def delete_item(request, id):
    item = get_object_or_404(CrochetItem, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'crochet_store/delete_confirm.html', {'item': item})
