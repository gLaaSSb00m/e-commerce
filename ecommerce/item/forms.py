from django import forms
from conversation.models import ConmversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model=ConmversationMessage
        fields=('content',)
        widgets={
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
        })
        }