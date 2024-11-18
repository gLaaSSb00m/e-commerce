from django.contrib import admin
from conversation.models import Conversation, ConmversationMessage

class ConversationMessageInline(admin.TabularInline):  # or admin.StackedInline
    model = ConmversationMessage
    extra = 1  # Number of empty forms to display for adding messages
    fields = ('content', 'created_by', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('item', 'created_at', 'modified_at')
    inlines = [ConversationMessageInline]  # Include messages inline
