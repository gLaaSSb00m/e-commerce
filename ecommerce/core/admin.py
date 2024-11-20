from django.contrib import admin
from conversation.models import Conversation, ConmversationMessage
from .models import Category,Customer,Product, Order
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
