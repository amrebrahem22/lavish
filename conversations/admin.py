from django.contrib import admin
from .models import Conversation, Message

class ConversationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'count_messages', 'count_participants')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created',)

admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Message, MessageAdmin)
