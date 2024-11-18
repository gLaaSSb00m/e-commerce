# views.py
from django.shortcuts import get_object_or_404, render,redirect
from itertools import zip_longest
from .models import Item, Catagory
from django.db.models import Q
from conversation.models import Conversation
from conversation.forms import ConmversationMessage, ConversationMessageForm
from item.models import Item


def items(request):
    query = request.GET.get('query', '')
    catagory_id = request.GET.get('category', 0)
    catagory = Catagory.objects.all()
    items = Item.objects.filter(is_sold=False)
    
    if catagory_id:
        items = items.filter(Catagory_id=catagory_id)  # Use 'Catagory_id' to match the actual field name in the database
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))  # Fixed 'description' typo
    
    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'catagory': catagory,
        'catagory_id': int(catagory_id),
    })

def detail(request, pk):
    # Fetch the item
    item = get_object_or_404(Item, pk=pk)

    

    # Retrieve or create a conversation for the current user and item
    conversation = Conversation.objects.filter(item=item, members=request.user).first()
    if not conversation:
        conversation = Conversation.objects.create(item=item)
        conversation.members.add(request.user)
        conversation.members.add(item.created_by)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            # Save the conversation message
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=pk)
    else:
        form = ConversationMessageForm()


    # Fetch related items
    related_items = Item.objects.filter(Catagory=item.Catagory, is_sold=False).exclude(pk=pk)
    paired_items = list(zip(*[iter(related_items)] * 2))  # Pair related items

    return render(request, 'item/detail.html', {
        'item': item,
        'paired_items': paired_items,
        'form': form,
    })
