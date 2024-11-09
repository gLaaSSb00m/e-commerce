from django.shortcuts import get_object_or_404, render
from itertools import zip_longest
from .models import Item
from django.contrib.auth.decorators import login_required
from.forms import NewItemForm

def items(request):
    items = Item.objects.filter(is_sold=False)
    
    return render(request, 'item/items.html',{
        'items': items,
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(Catagory=item.Catagory, is_sold=False).exclude(pk=pk)
    
    # Pair related items
    paired_items = list(zip_longest(*[iter(related_items)] * 2))
    
    return render(request, 'item/detail.html', {
        'item': item,
        'paired_items': paired_items,
    })

    
# Create your views here.
