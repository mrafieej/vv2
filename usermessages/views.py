from django.shortcuts import render
from django.views import generic
from .models import Message

class InboxView(generic.ListView):
    model = Message
    template_name = 'usermessages/inbox.html'

    def get_queryset(self):
        return Message.objects.filter(pk=1)  # TODO: change this

    def get_context_data(self, **kwargs):
        context = super(InboxView, self).get_context_data(**kwargs)
        context['loggedin'] = True
        return context

